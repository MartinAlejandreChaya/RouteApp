# Flask Template
Basic structure for starting a Flask project with Jinja templates

## Notas para todos

#### Interfaz de funciones

Para poder conectar todos los servicios desde el backend (es decir, recuperar las rutas, la información de clima para cada una de ellas, tráfico, ...) necesito que los objetos que devuelvan vuestras funciones sean consistentes. Por ello, la estructura que vamos a seguir es esta

```python
return {
   "success": True / False,
   "error_msg": "Mensaje de error si success == False",
   "data": {"Objeto que contenga los datos si success == True"}
}
```

Así yo podré hacer algo así:

```python
res = get_clima("navacerrada")
if (not res["success"]):
   # Devolver error al frontend
   return {"success": False, "error_msg": res["error_msg"]}

clima_data = res["data"]
# Continuar con ejecución normal del programa
```

*Por cierto, poner los mensajes de error en español*.

#### Deadlines

En Aula Global pone que el deadline es en 15 días (10 Diciembre). Por tanto, vamos a necesitar que vuestras funciones estén como tarde el **1 de Diciembre**. Tener en cuenta que también hay que entregar una memoria PDF y también hay que hacer la parte de Blockchain. La parte de Blockchain no sé cuando es el deadline, pero será parecido. El próximo día que quedemos vemos qué vamos a hacer para esa parte y cómo dividirnos un poco el trabajo, yo ya tengo alguna idea.

## Backend

- [ ] Scrappers
   - [ ] Route scrapper (Wikiloc) @Guille
   
- [ ] Api
   - [ ] Clima (Aemet) @Mar/@Laura
   - [ ] Tráfico (Google Maps) @Martin

- [ ] ETL Datawarehouse
   - [ ] Script de actualización (Airbnb) @Gabriel
   - [ ] Base de datos (Mongo) @Gabriel
   - [ ] Función que devuelva alojamientos cerca de una localización @Gabriel

- [ ] Integración de todo en el servidor @Martin

#### Frontend

- [ ] Route List Item (createRouteLi de route_renders.js)
- [ ] Route Item (createRouteItem de route_renders.js)
- [ ] Funcionalidades de Ordenar y Filtrar


---
### Setup the project for the first time

1. Clone this repository to local computer

2. Create a new virtual environment (takes a minute)
    - Windows:  ```python -m venv ./venv```
    - Mac:  ```python3 -m venv ./venv```

3. Activate the new virtual environment
   - Windows:
      - Require permission to activate: ```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser```
      -  Run activate script: ```.\venv\Scripts\activate```
   - Mac:  ```source ./venv/bin/activate```

4. Install the dependencies ```pip install -r requirements.txt```

5. Run the project with command: ```python app.py```

### Run the projec (subsequent times)

1. Activate virtual environment (if not already activated)

2. Run the project with ```python app.py```

### Github instructions

1. Work always on your own branch.

2. After finishing work on your branch, ask for review (via wassap for example).

3. After your branch has been reviewed you can merge into the main branch.

