from flask import Flask, request, jsonify
from flask_cors import CORS
from processor import process_input

app = Flask(__name__)
CORS(app)

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    mode = data.get("mode")
    text = data.get("text")

    result = process_input(mode, text)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)