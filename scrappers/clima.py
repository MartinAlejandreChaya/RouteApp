
# Script that gets the expected climate on location `loc` from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}
import json
from aemet import Aemet,Municipio, Prediccion
aemet_client=Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsYXVyYXNjMjAwMUBnbWFpbC5jb20iLCJqdGkiOiIxNjIyZmI4ZS05YWQ1LTQwOGMtODc1Zi1iNDU4OWY3NmQyMWMiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcwMDU4OTM5NSwidXNlcklkIjoiMTYyMmZiOGUtOWFkNS00MDhjLTg3NWYtYjQ1ODlmNzZkMjFjIiwicm9sZSI6IiJ9.-Ega71ci8LU5Ss2ZiYyRsyQQUEoHzisddpn9iH2BpU8')


if _name_ =='_clima_':
    ruta=''