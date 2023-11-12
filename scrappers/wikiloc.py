import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import lxml
import re


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}


URL="https://es.wikiloc.com/rutas-senderismo/risco-peluca-2-051-m-sierra-del-artunero-desde-el-puerto-de-mijares-8864179"
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
b=soup.find('p',string='Distancia')
print(b)
siguiente=b.find_next_sibling('span')
print(siguiente)
print(siguiente.text)

#print(soup.find_all('span'))

eu=soup.find("a", class_="btn btn-lg btn-success btn-download")
print(eu)
ref=eu.get("href")
print(ref)



class ruta:
    nombre = ""
    Distancia=0.0 #Km
    Desnivel_positivo=0.0 #m
    Dificultad_tecnica= ""
    Desnivel_negativo= 0.0 #m
    Altitud_maxima=0.0 #m
    Trailrank=0.0
    Estrellas=0.0
    Altitud_minima=0.0 #m
    Tipo_ruta=""
    Pagina_descarga=""

