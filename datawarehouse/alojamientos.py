from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/alojamientos"
mongo = PyMongo(app)

# Script that updates the datawarehouse by pulling from Airbnb
# Returns: True if success, False otherwise
@app.route("/update_accomodation")
def actualizar_datawarehouse():
    
    return True

def get_alojamientos(loc):

    return {
        "success": False,
        "error_msg": "Get alojamientos not implemented"
    }