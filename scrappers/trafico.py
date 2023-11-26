# Script that gets the traffic `loc` from Google Maps API

import googlemaps
from datetime import datetime


"""
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                         "Parramatta, NSW",
                                         mode="transit",
                                         departure_time=now)
    print(directions_result)

"""

# Returns {"long": , "lat": } of loc
def get_lat_long(address, gmaps):
    geocode_result = gmaps.geocode(address)
    if (len(geocode_result) == 0):
        return {"success": False, "error_msg": "La dirección " + address + " no es válida"}

    # Result is list of geocoding results
    res = geocode_result[0]["geometry"]["location"]
    return {
        "success": True,
        "loc": {"lat": res["lat"], "long": res["lng"]}
    }

# Returns Address of loc
def get_dir(loc, gmaps):
    reverse_geocode_result = gmaps.reverse_geocode((loc["lat"], loc["long"]))
    # Result is list of geocoding results
    if (len(reverse_geocode_result) == 0):
        return {"success": False, "error_msg": "La dirección " + loc["lat"] + ", " + loc["long"] + " no es valida"}

    res = reverse_geocode_result[0]["formatted_address"]

    return {
        "success": True,
        "address": res
    }


def get_traffic(from_loc, to_loc, gmaps):
    if (not from_loc["exists"]):
        return {
            "success": False,
            "error_msg": "Ubicación de partida no válida"
        }
    # Call google API

    return {
        "success": False,
        "error_msg": "Get traffic not implemented yet"
    }

