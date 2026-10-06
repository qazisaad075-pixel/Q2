from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Flask ML API"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    return jsonify({"status": "model prediction running", "input_data": data})

if __name__ == '__main__':
    app.run(debug=True)