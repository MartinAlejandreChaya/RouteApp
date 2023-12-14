from flask import Flask, request, jsonify
from flask import render_template, make_response
from datetime import datetime, date

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.headers["X-Frame-Options"] = ""
    return response



from scrappers.routes import get_routes
from scrappers.clima import get_clima
from scrappers.trafico import get_traffic, get_dir, get_lat_long
from datawarehouse.alojamientos import get_alojamientos

import googlemaps

@app.route("/search_routes", methods=["GET", "POST"])
def search():
    # Parameters
    params = request.get_json()

    # Place
    search_title = params["search_title"]
    gmaps = googlemaps.Client(key='AIzaSyBxkPLTw1AgCBl6wkOP9wu0_xaumdy7Kcc')
    search_loc = get_search_title_location(search_title, gmaps)
    if (not search_loc["exists"]):
        return {
            "success": False,
            "error_msg": search_loc["error_msg"]
        }
    place = {
        "search_title": search_title,
        "search_loc": search_loc
    }

    # route date
    route_date = datetime.now()
    if ("route_date" in params.keys()):
        param_date = datetime.strptime(params["route_date"], "%Y-%m-%d")
        today_date = datetime.today()
        today_date = date(today_date.year, today_date.month, today_date.day)
        o_date = date(param_date.year, param_date.month, param_date.day)
        if (o_date < today_date):
            return {
                "success": False,
                "error_msg": "La fecha propuesta es en el pasado"
            }
        elif (o_date >= today_date):
            route_date = param_date.replace(hour=route_date.hour, minute=route_date.minute)


    # from loc
    from_loc = {
        "exists": False,
        "error_msg": "Introduce ubicacion en busqueda"
    }
    if ("from_loc" in params.keys()):
        from_loc = get_from_loc_location(params["from_loc"], gmaps)


    print("Parameters:")
    print("\tPlace:", place)
    print("\tDate:", route_date)
    print("\tFrom loc:", from_loc)


    # Search for routes close to search_title
    routes_res = get_routes(place["search_loc"]["loc"])
    if (not routes_res["success"]):
        return jsonify({"success": False, "error_msg": routes_res["error_msg"]})
    routes = routes_res["data"]


    # Get climate in route
    for route in routes:
        # Set route init point dir
        if (route["route_data"]["punto_inicio"]):
            address_res = get_dir(route["route_data"]["punto_inicio"]["loc"], gmaps)
            if (address_res["success"]):
                route["route_data"]["punto_inicio"]["address"] = address_res["address"]
                route["route_data"]["punto_inicio"]["municipio"] = address_res["municipio"]
            else:
                route["route_data"]["punto_inicio"]["address"] = False
                route["route_data"]["punto_inicio"]["municipio"] = False

        clima_res = get_clima(route["route_data"]["punto_inicio"]["municipio"], route_date)
        # Date too far in the future error
        if (not clima_res["success"]):
            route["clima"] = False
            route["clima_error"] = clima_res["error_msg"]
        else:
            route["clima"] = clima_res["data"]


    # Get traffic in route
    for route in routes:
        traffic_res = get_traffic(from_loc, route["route_data"]["punto_inicio"], gmaps, route_date)

        # From loc not null error
        if (not traffic_res["success"]):
            route["traffic"] = False
            route["traffic_error"] = traffic_res["error_msg"]
        else:
            route["traffic"] = traffic_res["data"]


    # Get acomodation in route
    for route in routes:

        alojamientos_res = get_alojamientos(route["route_data"]["punto_inicio"]["municipio"])

        if (not alojamientos_res["success"]):
            route["alojamientos"] = False
            route["alojamientos_error"] = alojamientos_res["error_msg"]
        else:
            route["alojamientos"] = alojamientos_res["data"]



    return jsonify({
        "success": True,
        "routes": routes
    })



def get_search_title_location(search_title, gmaps):
    res = get_lat_long(search_title, gmaps)
    if (not res["success"]):
        return {
            "exists": False,
            "error_msg": res["error_msg"]
        }
    else:
        address = get_dir(res["loc"], gmaps)
        if (not address["success"]):
            return {
                "exists": False,
                "error_msg": "La dirección de búsqueda no es válida"
            }
        else:
            return {
                "exists": True,
                "loc": res["loc"],
                "address": address["address"]
            }

def get_from_loc_location(from_loc, gmaps):
    if (from_loc["geolocated"]):
        # We have coordinates in Lat, Long format
        loc_lat_long = from_loc["location_coords"]
        res = get_dir(loc_lat_long, gmaps)
        if (not res["success"]):
            return {
                "exists": False,
                "error_msg": res["error_msg"]
            }
        else:
            return {
                "exists": True,
                "loc": loc_lat_long,
                "address": res["address"]
            }
    else:
        loc_address = from_loc["location_title"]
        res = get_lat_long(loc_address, gmaps)
        if (not res["success"]):
            return {
                "exists": False,
                "error_msg": res["error_msg"]
            }
        else:
            return {
                "exists": True,
                "loc": res["loc"],
                "address": loc_address
            }


if __name__ == '__main__':
    app.run(debug=True)