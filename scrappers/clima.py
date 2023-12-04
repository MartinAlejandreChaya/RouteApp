
# Script that gets the expected climate on location `loc` from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}
import aemet.constants as cons
from aemet import Aemet,Municipio, Prediccion
aemet_client=Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsYXVyYXNjMjAwMUBnbWFpbC5jb20iLCJqdGkiOiIxNjIyZmI4ZS05YWQ1LTQwOGMtODc1Zi1iNDU4OWY3NmQyMWMiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTcwMDU4OTM5NSwidXNlcklkIjoiMTYyMmZiOGUtOWFkNS00MDhjLTg3NWYtYjQ1ODlmNzZkMjFjIiwicm9sZSI6IiJ9.-Ega71ci8LU5Ss2ZiYyRsyQQUEoHzisddpn9iH2BpU8')


#aemet_client = Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDA1MjcyODlAYWx1bW5vcy51YzNtLmVzIiwianRpIjoiNTg1OWIxNTUtYzQ1My00MjNmLWI0NDItYjBjOTdmNTA4ZTU1IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3MDExODQwODgsInVzZXJJZCI6IjU4NTliMTU1LWM0NTMtNDIzZi1iNDQyLWIwYzk3ZjUwOGU1NSIsInJvbGUiOiIifQ.u3_uZ0QIakpJOK2Dtdt3Vsyh1e0HdG066DDx8OUpPlA')

# Script that gets the expected climate on location loc from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}
def get_clima(loc,fecha_deseada):

    if (not loc):
        return {
            "success": False,
            "error_msg": "Ubicación de inicio de la ruta nó valida"
        }
    
    # Programa mar y laura
    muns = Municipio.buscar(loc) # muns es un objeto de la clase municipio por eso minima y maxima no la pillan que son objetos de la clase prediccionDia
    for i in range (0, len(muns)):
        # print(muns[i]) Voy a poner el get codigo porque me da un numero que puedo invocar en cualquier clase 
        idmuns = muns[i].get_codigo()
        #print(idmuns)
        predmuns = aemet_client.get_prediccion(idmuns, cons.PERIODO_DIA, True) # CUIDADO A VECES PONER AEMET.CLIENT Y NO AEMET
        
        #print(predmuns)
        #minima = predmuns.get_temperature_maxima()
        #print(minima)
        # montanya = aemet_client.get_prediccion_especifica_montanya(muns[i].getmunicipio, +1, True) 
        # print(montanya)   # El pesao de Gabriel dice que esto no esq no compile sino que no va pq soy inutil
    # minima = muns.get_temperatura_maxima()
    # maxima = muns.get_temperatura_minima()

    return {"success": False, "error_msg": "Clima function not implemented yet"}

get_clima("Málaga","2023-11-29")




 for dia in predmuns['prediccion']['dia']:
        if dia['fecha'] == fecha_deseada:
            informacion_tiempo = dia
            break

    # Verificar si se encontró información para la fecha deseada
    if informacion_tiempo:
        # Devolver la información del tiempo para el día seleccionado
        return {
            "fecha": fecha_deseada,
            "estado_cielo": informacion_tiempo['estadoCielo'][0]['descripcion'],
            "precipitacion": informacion_tiempo['precipitacion'][0]['value'],
            "prob_precipitacion": informacion_tiempo['probPrecipitacion'][0]['value'],
            "temp_max": informacion_tiempo['temperatura'][0]['max'],
            "temp_min": informacion_tiempo['temperatura'][0]['min'],
            "viento_max": informacion_tiempo['vientoAndRachaMax'][0]['velocidad'],
            "dir_viento_max": informacion_tiempo['vientoAndRachaMax'][0]['direccion'][0],
        }
    else:
        return None

# Uso del código
fecha_deseada = '2023-11-29'  # Puedes cambiar la fecha según tus necesidades
informacion_tiempo = obtener_informacion_tiempo(predmuns, fecha_deseada)

if informacion_tiempo:
    print(f"Información del tiempo para Málaga del Fresno el {informacion_tiempo['fecha']}:\n")
    print(f"Estado del cielo: {informacion_tiempo['estado_cielo']}")
    print(f"Precipitación: {informacion_tiempo['precipitacion']} mm")
    print(f"Probabilidad de precipitación: {informacion_tiempo['prob_precipitacion']}%")
    print(f"Temperatura máxima: {informacion_tiempo['temp_max']}°C")
    print(f"Temperatura mínima: {informacion_tiempo['temp_min']}°C")
    print(f"Viento máximo: {informacion_tiempo['viento_max']} km/h, dirección: {informacion_tiempo['dir_viento_max']}")
else:
    print(f"No se encontró información para la fecha {fecha_deseada}")