from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for orders
orders = []

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order = {
        "order_id": len(orders) + 1,
        "product_id": data.get("product_id"),
        "quantity": data.get("quantity")
    }
    orders.append(order)
    return jsonify(order), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
