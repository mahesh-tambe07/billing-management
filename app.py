from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Billing Management API is running!"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    # Example: assume data = {"items": [{"name": "Tea", "price": 10, "qty": 2}, {"name": "Coffee", "price": 20, "qty": 1}]}
    
    total = 0
    for item in data.get("items", []):
        total += item["price"] * item["qty"]
    
    return jsonify({"total": total})
