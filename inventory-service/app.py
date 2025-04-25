from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = {
    "item001": 100,
    "item002": 50
}

@app.route("/inventory/<item_id>", methods=["GET"])
def get_inventory(item_id):
    quantity = inventory.get(item_id, 0)
    return jsonify({"item_id": item_id, "quantity": quantity})

@app.route("/inventory/<item_id>", methods=["POST"])
def update_inventory(item_id):
    data = request.json
    inventory[item_id] = inventory.get(item_id, 0) + data.get("change", 0)
    return jsonify({"item_id": item_id, "quantity": inventory[item_id]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
