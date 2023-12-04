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

    municipio = False
    add_comp = reverse_geocode_result[0]["address_components"]
    for elem in add_comp:
        if ("locality" in elem["types"]):
            municipio = elem["long_name"]

    return {
        "success": True,
        "address": res,
        "municipio": municipio
    }


def get_traffic(from_loc, to_loc, gmaps, date=False):
    if (not from_loc["exists"]):
        return {"success": False, "error_msg": "Ubicación de partida no válida"}
    if (not to_loc):
        return {"success": False, "error_msg": "No se pudo recuperar el punto de inicio de ruta."}

    if (not date):
        date = datetime.now()

    # Call google API
    directions_result = gmaps.directions(from_loc["address"],
                                         to_loc["address"],
                                         mode="driving",
                                         departure_time=date,
                                         language="es")
    if (len(directions_result) == 0):
        print("Error in ", from_loc, " to ", to_loc)
        return {"success": False, "error_msg": "No se puede hallar ruta a punto especificado"}

    legs = directions_result[0]["legs"][0]
    steps = []
    for step in legs["steps"]:
        steps.append({
            "html_instructions": step["html_instructions"],
            "distance": step["distance"]
        })

    return {
        "success": True,
        "data": {
            "distance": legs["distance"],
            "duration": legs["duration"],
            "duration_in_traffic": legs["duration_in_traffic"],
            "steps": steps # {html_instructions, distance}
        }
    }
