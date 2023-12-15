import requests
import json
from datetime import datetime, timedelta
from bson import ObjectId, json_util
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['alojamientos']
collection = db['collection']

def insert_data_to_mongo():
    try:
        collection.delete_many({})
        with open('locations.json', 'r') as loc:
            locations = json.load(loc)

        with open('accomodations.json', 'w') as accoms:
            json.dump({}, accoms)

        for locs in locations.get('Poblacion'):
            get_accomodations(locs)

        # Lee los datos desde el archivo JSON
        with open('accomodations.json', 'r') as file:
            data = json.load(file)
            
        # Inserta los datos en la colección de MongoDB
        collection.insert_many(data)

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
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Agregar nuevos datos a los datos existentes
        existing_data.update(accomodations)

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
        total_accoms = []
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
            
            total_accoms.append(accomodations)
        return total_accoms
    else:
        print(f"Error en la solicitud. Código de estado: {response.status_code}")

insert_data_to_mongo()
