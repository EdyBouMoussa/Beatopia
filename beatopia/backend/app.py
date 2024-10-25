from flask import Flask, jsonify # type: ignore
from flask_cors import CORS   # type: ignore

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
