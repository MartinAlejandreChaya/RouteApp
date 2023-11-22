# Flask Template
Basic structure for starting a Flask project with Jinja templates

## TODOs

#### Backend

- [ ] Scrappers
   - [ ] Route scrapper (Wikiloc) @Guille
   
- [ ] Api
   - [ ] Clima (Aemet) @Mar/@Laura
   - [ ] Tráfico (Google Maps) @Martin

- [ ] ETL Datawarehouse
   - [ ] Script de actualización (Airbnb) @Gabriel
   - [ ] Base de datos (Mongo) @Gabriel

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

