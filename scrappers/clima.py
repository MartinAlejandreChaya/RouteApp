
# Script that gets the expected climate on location `loc` from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}
# from aemet import Aemet,Municipio,Prediccion
# aemet_client=Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsYXVyYXNjMjAwMUBnbWFpbC5jb20iLCJqdGkiOiIxNjIyZmI4ZS05YWQ1LTQwOGMtODc1Zi1iNDU4OWY3NmQyMWMiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcwMDU4OTM5NSwidXNlcklkIjoiMTYyMmZiOGUtOWFkNS00MDhjLTg3NWYtYjQ1ODlmNzZkMjFjIiwicm9sZSI6IiJ9.-Ega71ci8LU5Ss2ZiYyRsyQQUEoHzisddpn9iH2BpU8')


# Script that gets the expected climate on location `loc` from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}
def get_clima(loc, date):
    print(loc, date)
    if (not loc):
        return {
            "success": False,
            "error_msg": "Ubicación de inicio de la ruta nó valida"
        }

    # Programa mar y laura

    return {"success": False, "error_msg": "Clima function not implemented yet"}