
# Script that gets the expected climate on location `loc` from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}
import aemet.constants as cons
from aemet import Aemet, Municipio, Prediccion
from datetime import datetime, timedelta
import json
aemet_client=Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsYXVyYXNjMjAwMUBnbWFpbC5jb20iLCJqdGkiOiIxNjIyZmI4ZS05YWQ1LTQwOGMtODc1Zi1iNDU4OWY3NmQyMWMiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcwMDU4OTM5NSwidXNlcklkIjoiMTYyMmZiOGUtOWFkNS00MDhjLTg3NWYtYjQ1ODlmNzZkMjFjIiwicm9sZSI6IiJ9.-Ega71ci8LU5Ss2ZiYyRsyQQUEoHzisddpn9iH2BpU8')


#aemet_client = Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1MjcyODlAYWx1bW5vcy51YzNtLmVzIiwianRpIjoiNTg1OWIxNTUtYzQ1My00MjNmLWI0NDItYjBjOTdmNTA4ZTU1IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3MDExODQwODgsInVzZXJJZCI6IjU4NTliMTU1LWM0NTMtNDIzZi1iNDQyLWIwYzk3ZjUwOGU1NSIsInJvbGUiOiIifQ.u3_uZ0QIakpJOK2Dtdt3Vsyh1e0HdG066DDx8OUpPlA')

# Script that gets the expected climate on location loc from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}


#------------------------ Calculamos los dias de diiferencia entre la fecha introducida y la fecha actual------------------------
def days_from_today(date):
    # Get the date of today
    today = datetime.now()

    # Calcula la diferencia de días
    difference = date - today


    # Verifica si la diferencia es más de una semana
    if difference.days > 6 or difference.days < -1:
        return -1
    else:
        return difference.days+1




#---------------------------- Obtiene la predicción del día que se le introduce ----------------------
def get_weather_data(day_data):
    precipitacion = day_data.get('probPrecipitacion')
    cotanieve = day_data.get('cotaNieveProv')
    estadocielo = day_data.get('estadoCielo')
    viento = day_data.get('viento')
    temperatura= day_data.get('temperatura')
    sensacion=day_data.get('sensTermica')
    humedad= day_data.get('humedadRelativa')

    for val in estadocielo:
        if (val["descripcion"] != ""):
            estadocielo = val["descripcion"]
            break


    return {
        "Precipitacion": precipitacion[0].get('value'),
        "Probabilidad de nieve": cotanieve[0].get('value'),
        "Estado del cielo":estadocielo,
        "Viento":viento[0].get('velocidad'),
        "Temperatura":{"Maxima":temperatura.get('maxima'),"Minima":temperatura.get('minima')},
        "Sensacion termica":{"Maxima":sensacion.get('maxima'),"Minima":sensacion.get('minima')},
        "Humedad relativa":{"Maxima":humedad.get('maxima'),"Minima":humedad.get('minima')},
        "Radiacion UV maxima": day_data.get('uvMax')
    }

        

def get_clima(loc, date):

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
    
    mun = Municipio.buscar(loc) 
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

    return {
        "success": True,
        "data": weather_data
    }


