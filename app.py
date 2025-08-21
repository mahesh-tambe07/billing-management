from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Billing Management API is running!"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    total = 0
    for item in data.get("items", []):
        total += item["price"] * item["qty"]
    return jsonify({"total": total})

# Run the app only in local mode (Render will use gunicorn)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
