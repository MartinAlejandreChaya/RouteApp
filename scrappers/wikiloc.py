import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import lxml
import re

class ruta:
    nombre = ""
    Distancia="0.0" #Km
    Desnivel_positivo="0.0" #m
    Dificultad_tecnica= ""
    Desnivel_negativo= "0.0" #m
    Altitud_maxima="0.0" #m
    Trailrank="0.0"
    Estrellas="0.0"
    Altitud_minima="0.0" #m
    Tipo_ruta=""
    Pagina_descarga=""
    def __init__(self,nombre,Distancia,Desnivel_positivo,Dificultad_tecnica,Desnivel_negativo,Altitud_maxima,Trailrank,Estrellas,Altitud_minima,Tipo_ruta,Pagina_descarga) :
        self.nombre = nombre
        self.Distancia=Distancia
        self.Desnivel_positivo=Desnivel_positivo
        self.Dificultad_tecnica= Dificultad_tecnica
        self.Desnivel_negativo= Desnivel_negativo
        self.Altitud_maxima=Altitud_maxima
        self.Trailrank=Trailrank
        self.Estrellas=Estrellas
        self.Altitud_minima=Altitud_minima
        self.Tipo_ruta=Tipo_ruta
        self.Pagina_descarga=Pagina_descarga

    def mostrar(self):
        return ("Ruta: "  + self.nombre +"\nDistancia: " +self.Distancia+"\nDesnivel positivo: "+self.Desnivel_positivo+"\nDificultad tecnica: "+self.Dificultad_tecnica+"\nDesnivel_negativo: "+self.Desnivel_negativo+"\nAltitud maxima: "+self.Altitud_maxima+"\nTrailrank: "+self.Trailrank+"\nEstrellas: "+self.Estrellas+"\nAltitud minima: "+self.Altitud_minima+"\nTipo de ruta: "+self.Tipo_ruta+"\nPagina de descarga: "+self.Pagina_descarga)



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

URL="https://es.wikiloc.com/rutas-senderismo/torres-del-paine-refugio-paine-grande-a-refugio-grey-y-mirador-grey-y-vuelta-32629180"
def info(URL):
    nombre = "a"
    Distancia=0.0 #Km
    Desnivel_positivo=0.0 #m
    Dificultad_tecnica= "a"
    Desnivel_negativo= 0.0 #m
    Altitud_maxima=0.0 #m
    Trailrank=0.0
    Estrellas="-1.0"
    Altitud_minima=0.0 #m
    Tipo_ruta="a"
    Pagina_descarga="a"

    ruta1 = ruta(nombre,Distancia,Desnivel_positivo,Dificultad_tecnica,Desnivel_negativo,Altitud_maxima,Trailrank,Estrellas,Altitud_minima,Tipo_ruta,Pagina_descarga) 

    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    b=soup.find('p',string='Distancia')
    siguiente=b.find_next_sibling('span')
    ruta1.Distancia=siguiente.text.replace("\xa0"," ")
    b=soup.find('p',string='Desnivel positivo')
    siguiente=b.find_next_sibling('span')
    ruta1.Desnivel_positivo=siguiente.text.replace("\xa0"," ")

    b=soup.find('p',string='Dificultad técnica')
    siguiente=b.find_next_sibling('span')

    ruta1.Dificultad_tecnica=siguiente.text
    b=soup.find('p',string='Desnivel negativo')
    siguiente=b.find_next_sibling('span')

    ruta1.Desnivel_negativo=siguiente.text.replace("\xa0"," ")
    b=soup.find('p',string='Altitud máxima')
    siguiente=b.find_next_sibling('span')

    ruta1.Altitud_maxima=siguiente.text.replace("\xa0"," ")
    b=soup.find('p',string='Trailrank')
    siguiente=b.find_next_sibling('span')
    ruta1.Trailrank=siguiente.text.replace("\xa0"," ")

    try:
        b=soup.find("img", class_="d-item-star")
        c=b.parent
    except AttributeError as e:
        pass
        #print("no hay estrellas:",e)
    else:
        ruta1.Estrellas=c.text.replace("\xa0"," ")

    #print(c.text)
    b=soup.find('p',string='Altitud mínima')
    siguiente=b.find_next_sibling('span')
    ruta1.Altitud_minima=siguiente.text.replace("\xa0"," ")

    b=soup.find('p',string='Tipo de ruta')
    siguiente=b.find_next_sibling('span')
    ruta1.Tipo_ruta=siguiente.text



    #print(soup.find_all('span'))

    eu=soup.find("a", class_="btn btn-lg btn-success btn-download")
    ref=eu.get("href")
    ruta1.Pagina_descarga=ref


    u=soup.find("h1", class_="d-inline dont-break-out")
    nom=u.text.replace("\t","").replace("\n","")
    ruta1.nombre=nom

    print(ruta1.mostrar())
    return(ruta1)

ruta2=info(URL)
#print(ruta2.mostrar())

