from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for product inventory
inventory = {
    1: 10,  # Laptop stock
    2: 20,  # Phone stock
    3: 30   # Headphones stock
}

@app.route('/inventory/<int:product_id>', methods=['GET'])
def check_inventory(product_id):
    stock = inventory.get(product_id, 0)
    return jsonify({"product_id": product_id, "stock": stock})

@app.route('/inventory/<int:product_id>', methods=['POST'])
def update_inventory(product_id):
    data = request.get_json()
    quantity = data.get("quantity")
    if product_id in inventory:
        inventory[product_id] += quantity
        return jsonify({"product_id": product_id, "new_stock": inventory[product_id]})
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
