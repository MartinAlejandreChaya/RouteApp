
# Script that gets the expected climate on location `loc` from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}
from aemet import Aemet,Municipio,Prediccion
aemet_client=Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsYXVyYXNjMjAwMUBnbWFpbC5jb20iLCJqdGkiOiIxNjIyZmI4ZS05YWQ1LTQwOGMtODc1Zi1iNDU4OWY3NmQyMWMiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcwMDU4OTM5NSwidXNlcklkIjoiMTYyMmZiOGUtOWFkNS00MDhjLTg3NWYtYjQ1ODlmNzZkMjFjIiwicm9sZSI6IiJ9.-Ega71ci8LU5Ss2ZiYyRsyQQUEoHzisddpn9iH2BpU8')

def get_clima():
    muns=Municipio.buscar('Manresa')
    print(Municipio.get_municipio('08113'))
    
    # Programa mar y laura22

    #return {"success": False, "error_msg": "Clima function not implemented yet"}
get_clima()