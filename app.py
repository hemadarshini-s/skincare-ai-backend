import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Read secret key from environment (Render → Environment Variables)
app.secret_key = os.environ.get("SECRET_KEY", "dev-fallback-key")

@app.route("/")
def home():
    return "Flask app is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        product = data.get("product", "").lower()
        time = data.get("time", "").lower()

        if "salicylic acid" in product and "retinol" in product:
            return jsonify({
                "product": "salicylic acid and retinol",
                "time": time,
                "warnings": ["Avoid using salicylic acid and retinol together."],
                "recommendations": [
                    "Use salicylic acid in the morning with sunscreen.",
                    "Use retinol at night to avoid sun sensitivity."
                ],
                "note": "Both are strong actives and can cause irritation if combined."
            })

        # If no interaction warning
        return jsonify({
            "product": product,
            "time": time,
            "warnings": [],
            "recommendations": ["No harmful interactions detected."],
            "note": "Safe to use."
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

