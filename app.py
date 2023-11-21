from flask import Flask, request, jsonify
from flask import render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


from scrappers.routes import get_routes, get_coordinates
from scrappers.clima import get_clima
from scrappers.trafico import get_traffic

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
    from_loc = False
    if ("from_loc" in params.keys()):
        from_loc = params["from_loc"]
        if (from_loc["geolocated"]):
            from_loc = from_loc["location_coords"]
        else:
            from_loc_res = get_coordinates(from_loc["location_title"])
            if (not from_loc_res["success"]):
                return jsonify({"success": False, "error_msg": from_loc_res["error_msg"]})
            from_loc = from_loc_res["coords"]

    print("Parameters:")
    print("\tPlace:", search_title)
    print("\tDate:", route_date)
    print("\tFrom loc:", from_loc)


    # Search for routes close to search_title
    routes_res = get_routes(search_title)
    if (not routes_res["success"]):
        return jsonify({"success": False, "error_msg": routes_res["error_msg"]})
    routes = routes_res["routes_data"]


    # Get climate in route
    for route in routes:

        clima_res = get_clima(route["location"])
        # Date too far in the future error
        if (not clima_res["success"]):
            route["clima"] = False
            route["clima_error"] = clima_res["error_msg"]
        else:
            route["clima"] = clima_res["clima_data"]


    # Get traffic in route
    for route in routes:

        traffic_res = get_traffic(from_loc, route["location"])
        # From loc not null error
        if (not traffic_res["success"]):
            route["traffic"] = False
            route["traffic_error"] = traffic_res["error_msg"]
        else:
            route["traffic"] = traffic_res["route_data"]



    return jsonify({
        "success": True,
        "routes": routes
    })


if __name__ == '__main__':
    app.run(debug=True)