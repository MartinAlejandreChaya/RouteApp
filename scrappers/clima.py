
# Script that gets the expected climate on location `loc` from aemet API
# Returns: {"sucess": True/False, "climate": climate_data}
def get_clima(loc):

    if (not loc):
        return {
            "success": False,
            "error_msg": "Ubicación de inicio de la ruta nó valida"
        }
    
    # Programa mar y laura

    return {"success": False, "error_msg": "Clima function not implemented yet"}
