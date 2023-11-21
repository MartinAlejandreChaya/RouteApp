from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/search_routes", methods=["GET", "POST"])
def search():
    search_title = request.get_json()["search_title"]

    routes = [
            {
                "titulo": search_title,
                "dificultad": "hard",
                "longitud": "20km",
                "clima": "soleado",
                "tiempo_transporte": "3h30m"
            },
            {
                "titulo": search_title + " test",
                "dificultad": "fácil",
                "longitud": "5km",
                "clima": "nublado",
                "tiempo_transporte": "1h20m"
            },
            {
                "titulo": search_title + " test2",
                "dificultad": "fácil",
                "longitud": "5km",
                "clima": "nublado",
                "tiempo_transporte": "1h20m"
            }
        ]
    return jsonify({
        "success": True,
        "routes": routes
    })


if __name__ == '__main__':
    app.run(debug=True)