import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import lxml
import re
from selenium import webdriver
from selenium.webdriver.edge.options import Options



class ruta: #Aquí se ve toda la información que tomamos de cada ruta

    nombre = "" #Ten en cuenta que todo se gurada como un string
    Punto_inicio="0.0,0.0" #Tambien un solo string !!!
    Distancia="0.0 Km" 
    Desnivel_positivo="0.0 m"
    Dificultad_tecnica= ""
    Desnivel_negativo= "0.0 m"
    Altitud_maxima="0.0 m"
    Trailrank="0.0"
    Estrellas="-1.0" #Si no tiene calificación en estrellas saldrá -1
    Altitud_minima="0.0 m"
    Tipo_ruta=""
    Pagina_descarga="" #aquí está la pagina para encontrar la ruta
    
    def __init__(self,nombre,Distancia,Desnivel_positivo,Dificultad_tecnica,Desnivel_negativo,Altitud_maxima,Trailrank,Estrellas,Altitud_minima,Tipo_ruta,Pagina_descarga,Punto_inicio):
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
        self.Punto_inicio=Punto_inicio

    def mostrar(self):
        return ("Ruta: " + self.nombre +"\nDistancia: " +self.Distancia+"\nDesnivel positivo: "+self.Desnivel_positivo+"\nDificultad tecnica: "+self.Dificultad_tecnica+"\nDesnivel_negativo: "+self.Desnivel_negativo+"\nAltitud maxima: "+self.Altitud_maxima+"\nTrailrank: "+self.Trailrank+"\nEstrellas: "+self.Estrellas+"\nAltitud minima: "+self.Altitud_minima+"\nTipo de ruta: "+self.Tipo_ruta+"\nPagina de descarga: "+self.Pagina_descarga+"\nPunto de inicio: "+self.Punto_inicio)

#URL="https://es.wikiloc.com/rutas-senderismo/torres-del-paine-refugio-paine-grande-a-refugio-grey-y-mirador-grey-y-vuelta-32629180"

def info(URL): #Yo ni abriria esto, te devuelve toda la informacion de una ruta en concreto

    #Predefinimos las variables por si hay algun error luego al encontrarlas
    nombre = "" 
    Punto_inicio="0.0,0.0" 
    Distancia="0.0 Km" 
    Desnivel_positivo="0.0 m"
    Dificultad_tecnica= ""
    Desnivel_negativo= "0.0 m"
    Altitud_maxima="0.0 m"
    Trailrank="0.0"
    Estrellas="-1.0" #Si no tiene calificación en estrellas saldrá -1.0
    Altitud_minima="0.0 m"
    Tipo_ruta=""
    Pagina_descarga=""

    ruta1 = ruta(nombre,Distancia,Desnivel_positivo,Dificultad_tecnica,Desnivel_negativo,Altitud_maxima,Trailrank,Estrellas,Altitud_minima,Tipo_ruta,Pagina_descarga,Punto_inicio) 

    headers = {'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko)'}
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    b=soup.find('p',string='Distancia')
    siguiente=b.find_next_sibling('span')
    ruta1.Distancia=siguiente.text.replace("\xa0"," ") #Te viene con el símbolo del caracter para el espacio "0.0\xa0km", así se te queda "0.0 km"

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
        #print(b)
        c=b.parent
        #print(c.text)
    except AttributeError:
        ruta1.Estrellas="-1.0"
        #print("no hay estrellas")
    else:
        ruta1.Estrellas=c.text.replace("\xa0"," ")

    #print(c.text)
    b=soup.find('p',string='Altitud mínima')
    siguiente=b.find_next_sibling('span')
    ruta1.Altitud_minima=siguiente.text.replace("\xa0"," ")

    b=soup.find('p',string='Tipo de ruta')
    siguiente=b.find_next_sibling('span')
    ruta1.Tipo_ruta=siguiente.text


    b=soup.find('input',id="end-direction")
    siguiente=b.get('value')
    ruta1.Punto_inicio=siguiente


    #print(soup.find_all('span'))

    eu=soup.find("a", class_="btn btn-lg btn-success btn-download")
    ref=eu.get("href")
    ruta1.Pagina_descarga=ref


    u=soup.find("h1", class_="d-inline dont-break-out")
    nom=u.text.replace("\t","").replace("\n","")
    ruta1.nombre=nom

    #print(ruta1.mostrar())
    return(ruta1)

#ruta2=info(URL)
#print(ruta2.mostrar())

coords=[40.84,-5.87,40.86,-5.838] #coordenadas de ejemplo, se las tienes que meter en este formato. 
#Busca en un cuadrado con el primer punto el de abajo izquierda y el segundo el de arriba derecha.
#Si tienes un punto desplazalo -0.1,-0.1 para el primero y 0.1,0.1 para el segundo y te encontrara rutas en un entorno cercano.

def busqueda(coords): #Esta es la funcion que te interesa, te devuelve un array con todas las rutas encontradas

    #print(coords)
    URL2="https://es.wikiloc.com/wikiloc/map.do?sw="+str(coords[0])+'%2C'+str(coords[1])+'&ne='+str(coords[2])+'%2C'+str(coords[3])
    #print(URL2)
    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Edge(options=options)
    driver.get(URL2)
    html = driver.page_source

    soup2 = BeautifulSoup(html, 'lxml')

    #soup2 = BeautifulSoup(r.text, 'lxml')



    hrefs = [div.find("a").get("href") for div in soup2.find_all("div", class_="trail-card__title-wrapper")]
    #print(hrefs)
    rutas=[]
    for i in range(0,min(len(hrefs),30)):
        URL='https://es.wikiloc.com/'+hrefs[i]
        ruta2=info(URL)
        rutas.append(ruta2)
    if rutas!=[] and len(rutas)!=0:
        success=True
    else:
        success=False

    return {

   "success": success,
   "error_msg": "No ha encontrado ninguna ruta",
   "data": rutas #Te devuelve un array con todas las rutas que ha encontrado
    }

misrutas=busqueda(coords)

for refg in misrutas["data"]:
    print(refg.Punto_inicio)
print(misrutas["data"][3].Estrellas)
