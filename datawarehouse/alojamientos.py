import requests
import json
from datetime import datetime, timedelta

# Configura la conexión a MongoDB
DEV = True

if (not DEV):
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client['alojamientos']
    collection = db['collection']

def get_alojamientos(loc):
    """ try:
        # Busca todos los documentos que contienen el valor en el campo 'city'
        result = collection.find({"city": loc})

        # Convierte el resultado a una lista de diccionarios
        data_list = list(result)

        return {"success": True, "data": data_list}
    except Exception as e:
        return {"success": False, "error_msg": "Alojamiento para municipio " + loc + " no disponible en la base de datos"} """
    min_price = 123.12
    return {
        "success": True,
        "data": {
            "list": [
                {
                    "accommodation_type_name": "Otro alojamiento",
                    "latitude": 41.4658352733754,
                    "longitude": 1.82865500450134,
                    "hotel_id": 1839613,
                    "main_photo_url": "https://cf.bstatic.com/xdata/images/hotel/square60/87453742.jpg?k=546b61dd65eebc565bbf6b76db63bf4f928797b64de01e28f11b23f0bd417896&o=",
                    "hotel_name": "Masia Can Canyes & Spa",
                    "url": "https://www.booking.com/hotel/es/masia-can-canyes-1712.html",
                    "checkout": {
                        "from": "06:00",
                        "until": "12:00"
                    },
                    "checkin": {
                        "from": "15:00",
                        "until": "21:30"
                    },
                    "review_score": 9.4,
                    "city": [
                        "San Lorenzo de Hortons"
                    ],
                    "address": "Cami de Can Canyes s/n Masia - Alt Pened\u00e8s",
                    "district": "",
                    "price_breakdown": {
                        "has_tax_exceptions": 0,
                        "has_incalculable_charges": 0,
                        "all_inclusive_price": 128.68,
                        "gross_price": 127.58,
                        "sum_excluded_raw": "1.10",
                        "has_fine_print_charges": 1,
                        "currency": "EUR"
                    }
                },
                {
                    "accommodation_type_name": "Casas rurales",
                    "latitude": 41.4658352733754,
                    "longitude": 1.82865500450134,
                    "hotel_id": 1839613,
                    "main_photo_url": "https://cf.bstatic.com/xdata/images/hotel/square60/87453742.jpg?k=546b61dd65eebc565bbf6b76db63bf4f928797b64de01e28f11b23f0bd417896&o=",
                    "hotel_name": "Masia Can Canyes & Spa",
                    "url": "https://www.booking.com/hotel/es/masia-can-canyes-1712.html",
                    "checkout": {
                        "from": "06:00",
                        "until": "12:00"
                    },
                    "checkin": {
                        "from": "15:00",
                        "until": "21:30"
                    },
                    "review_score": 9.4,
                    "city": [
                        "San Lorenzo de Hortons"
                    ],
                    "address": "Cami de Can Canyes s/n Masia - Alt Pened\u00e8s",
                    "district": "",
                    "price_breakdown": {
                        "has_tax_exceptions": 0,
                        "has_incalculable_charges": 0,
                        "all_inclusive_price": 128.68,
                        "gross_price": 127.58,
                        "sum_excluded_raw": "1.10",
                        "has_fine_print_charges": 1,
                        "currency": "EUR"
                    }
                }
            ],
            "min_price": {
                "value": 123.53,
                "currency": "EUR"
            }
        }
    }

def insert_data_to_mongo():
    try:
        collection.delete_many({})
        with open('locations.json', 'r') as loc:
            locations = json.load(loc)

        with open('accomodations.json', 'w') as accoms:
            json.dump({}, accoms)

        #for locs in locations.get('Poblacion'):
        get_accomodations("Navacerrada")

        # Lee los datos desde el archivo JSON
        with open('accomodations.json', 'r') as file:
            data = json.load(file)
#        print(data)
        # Inserta los datos en la colección de MongoDB
        collection.insert_one(data)

    except Exception as e:
        print("success: ", False, "error: ", str(e))

def get_location_id(location):
    url = "https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete"
    querystring = {"text": location, "languagecode": "es"}
    headers = {
        "X-RapidAPI-Key": "482484a73dmshfbc6aab40de78bbp1ff607jsn0e5a948d687d",
        "X-RapidAPI-Host": "apidojo-booking-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el JSON de la respuesta
        json_data = response.json()

        # Verificar si la lista de objetos está presente en el JSON
        if isinstance(json_data, list):
            # Crear una lista para almacenar los dest_id
            destinations = []

            # Iterar sobre los objetos y almacenar los dest_id en la lista
            for result in json_data:
                dest_id = result.get('dest_id')
                dest_type = result.get('dest_type')
                if dest_id is not None and dest_type is not None:
                    destinations.append({"dest_id": dest_id, "dest_type": dest_type})

            # Guardar la información combinada en el archivo accomodations.json
            with open('destinations.json', 'w') as destinations_file:
                json.dump(destinations, destinations_file, indent=2)
                
        else:
            print("La estructura del JSON no es la esperada (no es una lista de objetos).")
    else:
        print(f"Error en la solicitud. Código de estado: {response.status_code}")

def get_accomodations(destination):

    get_location_id(destination)

    url = "https://apidojo-booking-v1.p.rapidapi.com/properties/list"
    # Obtener la fecha de hoy
    today = datetime.now().date()

    # Obtener la fecha de mañana
    tomorrow = today + timedelta(days=1)

    # Formatear las fechas en el formato deseado
    today_str = today.strftime('%Y-%m-%d')
    tomorrow_str = tomorrow.strftime('%Y-%m-%d')

    try:
        # Cargar los parámetros id y type desde el archivo JSON
        with open('destinations.json', 'r') as file:
            destination_data = json.load(file)

        for result in destination_data:
            dest_id = result.get('dest_id')
            dest_type = result.get('dest_type')

            # Verificar si dest_id y dest_type están presentes en el archivo JSON
            if dest_id is not None and dest_type is not None:
                querystring = {
                    "offset": "0",
                    "arrival_date": today_str,
                    "departure_date": tomorrow_str,
                    "guest_qty": "1",
                    "dest_ids": dest_id,
                    "room_qty": "1",
                    "search_type": dest_type,
                    "search_id": "none",
                    "price_filter_currencycode": "USD",
                    "order_by": "popularity",
                    "languagecode": "es",
                }

                headers = {
                    "X-RapidAPI-Key": "482484a73dmshfbc6aab40de78bbp1ff607jsn0e5a948d687d",
                    "X-RapidAPI-Host": "apidojo-booking-v1.p.rapidapi.com"
                }

                response = requests.get(url, headers=headers, params=querystring)

                accomodations = parse_accoms_json(response, destination)

            else:
                print("Error: dest_id or dest_type not present in destination.json")

        # Cargar datos existentes del archivo accomodations.json, si existe
        try:
            with open('accomodations.json', 'r') as accomodations_file:
                existing_data = json.load(accomodations_file)
                print("abierto accoms")
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []
            print("no se abre")

        # Agregar nuevos datos a los datos existentes
        existing_data.update(accomodations)
        #combined_data = existing_data + accomodations

        # Guardar la información combinada en el archivo accomodations.json
        with open('accomodations.json', 'w') as accomodations_file:
            json.dump(existing_data, accomodations_file, indent=2)

    except Exception as e:
        print(f"Error: {e}")

def parse_accoms_json(response, dest):

    if response.status_code == 200:
        json_data = response.json()
        # Asegúrate de entender la estructura de la respuesta JSON y ajustar esto
        results = json_data.get('result', [])

        for res in results:

            type = res.get('accommodation_type_name')
            latitude = res.get('latitude')
            longitude = res.get('longitude')
            id = res.get('hotel_id')
            photo = res.get('main_photo_url')
            name = res.get('hotel_name')
            url = res.get('url')
            checkout = res.get('checkout')
            checkin = res.get('checkin')
            score = res.get('review_score')
            city = dest,
            address = res.get('address')
            district = res.get('district')
            price = res.get('price_breakdown')

            accomodations = {"accommodation_type_name": type, "latitude": latitude, "longitude": longitude, "hotel_id": id, 
                              "main_photo_url": photo, "hotel_name": name, "url": url, "checkout": checkout, "checkin": checkin,
                              "review_score": score, "city": city, "address": address, "district": district, "price_breakdown": price}
    else:
        print(f"Error en la solicitud. Código de estado: {response.status_code}")
    return accomodations


if (not DEV):
    insert_data_to_mongo()
