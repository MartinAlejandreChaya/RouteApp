
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import lxml
import re
from selenium import webdriver
from selenium.webdriver.edge.options import Options


# PARAMS: The location around which we want to search for routes. Format (lat, long)
# RETURNS: A list of routes
def get_rutas(loc):

    # Build square
    coords = [loc[0], loc[1], loc[0] + 0.1, loc[1] + 0.1]

    # Get routes close to loc url:
    URL="https://es.wikiloc.com/wikiloc/map.do?sw="+str(coords[0])+'%2C'+str(coords[1])+'&ne='+str(coords[2])+'%2C'+str(coords[3])
    print("Getting routes from", URL)

    # BeautifoulSoup configuration
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Edge(options=options)
    driver.get(URL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    # Get all results within page
    hrefs = [div.find("a").get("href") for div in soup.find_all("div", class_="trail-card__title-wrapper")]

    if (len(hrefs) == 0):
        return {
            "success": False,
            "error_msg": "Ninguna ruta encontrada para la ubicación dada"
        }

    rutas = []
    for i in range(0, min(len(hrefs), 30)):
        ROUTE_URL = 'https://es.wikiloc.com/' + hrefs[i]
        route_info = get_route(ROUTE_URL)
        rutas.append({
            "route_data": route_info
        })

    return {
        "success": True,
        "route_data": rutas
    }


# Get info of specific route
def get_route(URL):
    print("Getting route info from ", URL)
    # Configure BeautifoulSoup
    headers = {'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko)'}
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    distancia = get_span_content("Distancia", soup)
    desnivel_positivo = get_span_content("Desnivel positivo", soup)
    dificultad_tecnica = get_span_content("Dificultad técnica", soup)
    desnivel_negativo = get_span_content("Desnivel negativo", soup)
    altitud_maxima = get_span_content("Altitud máxima", soup)
    trailrank = get_span_content("Trailrank", soup)
    altitud_minima = get_span_content("Altitud mínima", soup)
    tipo_ruta = get_span_content("Tipo de ruta", soup)

    # Nombre
    try:
        b = soup.find("h1", class_="d-inline dont-break-out")
        nombre = b.text.replace("\t", "").replace("\n", "")
    except:
        nombre = False

    # Punto inicio
    try:
        b = soup.find('input', id="end-direction")
        punto_inicio = b.get('value')
    except:
        punto_inicio = False

    # Página descarga
    try:
        b = soup.find("a", class_="btn btn-lg btn-success btn-download")
        pagina_descarga = b.get("href")
    except:
        pagina_descarga = False

    # Estrellas
    try:
        b = soup.find("img", class_="d-item-star")
        estrellas = b.parent.text.replace("\xa0"," ")
    except:
        estrellas = False

    return {
        "nombre": nombre,
        "punto_inicio": punto_inicio,
        "pagina_descarga": pagina_descarga,
        "estrellas": estrellas,
        "distancia": distancia,
        "desnivel_positivo": desnivel_positivo,
        "dificultad_tecnica": dificultad_tecnica,
        "desnivel_negativo": desnivel_negativo,
        "altitud_maxima": altitud_maxima,
        "altitud_minima": altitud_minima,
        "trailrank": trailrank,
        "tipo_ruta": tipo_ruta
    }

def get_span_content(name, soup):
    try:
        b = soup.find('p', string=name)
        siguiente = b.find_next_sibling('span')
        return siguiente.text.replace("\xa0", " ")
    except:
        return False


