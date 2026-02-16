from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {"id": 1, "name": "Цемент М500", "price": 850, "unit": "мешок"},
    {"id": 2, "name": "Кирпич красный", "price": 95, "unit": "шт"},
    {"id": 3, "name": "Доска обрезная", "price": 1250, "unit": "м3"}
]

@app.route('/')
def home():
    return jsonify({"message": "СтройМаркет API работает!", "status": "online"})

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/delivery/order', methods=['POST'])
def delivery_order():
    data = request.json
    return jsonify({"status": "success", "message": "Машина заказана!"})

@app.route('/api/loaders/order', methods=['POST'])
def loaders_order():
    data = request.json
    return jsonify({"status": "success", "message": "Грузчики заказаны!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
