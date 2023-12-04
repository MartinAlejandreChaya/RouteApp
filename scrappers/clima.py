
# Script that gets the expected climate on location `loc` from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}
import aemet.constants as cons
from aemet import Aemet, Municipio, Prediccion
aemet_client=Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsYXVyYXNjMjAwMUBnbWFpbC5jb20iLCJqdGkiOiIxNjIyZmI4ZS05YWQ1LTQwOGMtODc1Zi1iNDU4OWY3NmQyMWMiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcwMDU4OTM5NSwidXNlcklkIjoiMTYyMmZiOGUtOWFkNS00MDhjLTg3NWYtYjQ1ODlmNzZkMjFjIiwicm9sZSI6IiJ9.-Ega71ci8LU5Ss2ZiYyRsyQQUEoHzisddpn9iH2BpU8')


#aemet_client = Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1MjcyODlAYWx1bW5vcy51YzNtLmVzIiwianRpIjoiNTg1OWIxNTUtYzQ1My00MjNmLWI0NDItYjBjOTdmNTA4ZTU1IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3MDExODQwODgsInVzZXJJZCI6IjU4NTliMTU1LWM0NTMtNDIzZi1iNDQyLWIwYzk3ZjUwOGU1NSIsInJvbGUiOiIifQ.u3_uZ0QIakpJOK2Dtdt3Vsyh1e0HdG066DDx8OUpPlA')

# Script that gets the expected climate on location loc from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}
def get_clima(loc, date):
    # loc = nombre municipio
    if (not loc):
        return {
            "success": False,
            "error_msg": "Ubicación de inicio de la ruta nó valida"
        }

    # Comprobar si el día es entre hoy y dentro de siete días
    days_f_today = days_from_today(date)
    # Returns number of days between today and date
    # or -1 if date is not valid (before today or after more than 7 days)
    if (days_f_today == -1):
        return {
            "success": False,
            "error_msg": "No se puede obtener predicción para la fecha especificada"
        }
    
    # Programa mar y laura
    mun = Municipio.buscar(loc) # muns es un objeto de la clase municipio por eso minima y maxima no la pillan que son objetos de la clase prediccionDia

    if (len(mun) == 0):
        return {
            "success": False,
            "error_msg": "Municipio " + loc + " no encontrado"
        }

    municipio = mun[0]
    idmun = municipio.get_codigo()

    predmun = aemet_client.get_prediccion(idmun, cons.PERIODO_SEMANA, True)
    our_day = predmun["prediccion"]["dia"][days_f_today]

    weather_data = get_weather_data(our_day)

    for key in our_day:
        print("KEY: ", key)
        print(our_day[key])

    return {
        "success": True,
        "data": weather_data
    }





def days_from_today(date):

    return 2

def get_weather_data(day_data):

    return {
        "Probabilidad de precipitacion": day_data["probPrecipitacion"][0]["value"],
        "Estado del cielo": day_data["estadoCielo"][0]["descripcion"],
        "Humedad relativa": {
            "minimo": 1234,
            "maximo": 1234
        }
    }

get_clima("Málaga","2023-12-04")
