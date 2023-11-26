from flask import Flask, request, jsonify
from flask import render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


from scrappers.routes import get_routes
from scrappers.clima import get_clima
from scrappers.trafico import get_traffic, get_dir, get_lat_long
from datawarehouse.alojamientos import get_alojamientos

import googlemaps

@app.route("/search_routes", methods=["GET", "POST"])
def search():
    # Parameters
    params = request.get_json()
    search_title = params["search_title"]

    # route date
    route_date = date.today()
    if ("route_date" in params.keys()):
        route_date = params["route_date"]

    # from loc
    from_loc = {
        "exists": False,
        "error_msg": "Introduce ubicacion en busqueda"
    }
    if ("from_loc" in params.keys()):

        from_loc = params["from_loc"]
        if (from_loc["geolocated"]):
            # We have coordinates in Lat, Long format
            loc_lat_long = from_loc["location_coords"]
            res = get_dir(loc_lat_long, gmaps)
            if (not res["success"]):
                from_loc = {
                    "exists": False,
                    "error_msg": res["error_msg"]
                }
            else:
                from_loc = {
                    "exists": True,
                    "loc": loc_lat_long,
                    "address": res["address"]
                }

        else:
            loc_address = from_loc["location_title"]
            res = get_lat_long(loc_address, gmaps)
            if (not res["success"]):
                from_loc = {
                    "exists": False,
                    "error_msg": res["error_msg"]
                }
            else:
                from_loc = {
                    "exists": True,
                    "loc": res["loc"],
                    "address": loc_address
                }

    print("Parameters:")
    print("\tPlace:", search_title)
    print("\tDate:", route_date)
    print("\tFrom loc:", from_loc)


    # Search for routes close to search_title
    routes_res = get_routes(search_title)
    if (not routes_res["success"]):
        return jsonify({"success": False, "error_msg": routes_res["error_msg"]})
    routes = routes_res["data"]


    # Get climate in route
    for route in routes:

        clima_res = get_clima(route["location"])
        # Date too far in the future error
        if (not clima_res["success"]):
            route["clima"] = False
            route["clima_error"] = clima_res["error_msg"]
        else:
            route["clima"] = clima_res["data"]


    # Get traffic in route
    for route in routes:

        traffic_res = get_traffic(from_loc, route["location"])
        # From loc not null error
        if (not traffic_res["success"]):
            route["traffic"] = False
            route["traffic_error"] = traffic_res["error_msg"]
        else:
            route["traffic"] = traffic_res["data"]


    # Get acomodation in route
    for route in routes:

        alojamientos_res = get_alojamientos(route["location"])

        if (not alojamientos_res["success"]):
            route["alojamientos"] = False
            route["alojamientos_error"] = alojamientos_res["error_msg"]
        else:
            route["alojamientos"] = alojamientos_res["data"]


    return jsonify({
        "success": True,
        "routes": routes
    })


if __name__ == '__main__':
    app.run(debug=True)