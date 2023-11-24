
# Script that gets the traffic `loc` from Google Maps API
import googlemaps
from datetime import datetime



# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# print(reverse_geocode_result)

# Request directions via public transit
if (False):
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                         "Parramatta, NSW",
                                         mode="transit",
                                         departure_time=now)
    print(directions_result)

    # Validate an address with address validation
    addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'],
                                                        regionCode='US',
                                                        locality='Mountain View',
                                                        enableUspsCass=True)
    print(addressvalidation_result)

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

    # Call google API

    return {
        "success": False,
        "traffic": {}
    }

