# Multi-tracker-product-data-service

from flask import Flask, jsonify

app = Flask(__name__)

# Example product data
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500},
    {"id": 3, "name": "Headphones", "price": 150}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
