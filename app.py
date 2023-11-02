from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/search_routes", methods=["GET", "POST"])
def search():
    search_title = request.get_json()["search_title"]

    return jsonify({
        "res": "Server response from page " + search_title
    })


if __name__ == '__main__':
    app.run(debug=True)