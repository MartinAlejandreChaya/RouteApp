import requests
import json
from datetime import datetime, timedelta
from bson import ObjectId, json_util
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['alojamientos']
collection = db['collection']

def get_alojamientos(loc):
    try:
        # Busca todos los documentos que contienen el valor en el campo 'city'
        result_count = collection.count_documents({"city": loc})
        if result_count == 0:
            return {"success": False, "error_msg": "Alojamiento para municipio " + loc + " no disponible en la base de datos"}
        result = collection.find({"city": loc})

        # Convierte el resultado a una lista de diccionarios
        final_res = parse_data(result)
        print(final_res)
        return {"success": True, "data": final_res}
    except Exception as e:
        print(e)
        return {"success": False, "error_msg": "Alojamiento para municipio " + loc + " no disponible en la base de datos"}
    
def parse_data(result):
    parsed_list = []
    min_price = float(10000)
    
    for document in result:
        doc = json.loads(json_util.dumps(document))
        price_item = doc.get('price_breakdown')
        price = float(price_item["gross_price"])
        if (price < min_price):
            min_price = price
        
        parsed_list.append(doc)
    
    result_data = {
        "list": parsed_list,
        "min_price": {
            "value": min_price,
            "currency": "EUR"
        }
    }
    
    return result_data
