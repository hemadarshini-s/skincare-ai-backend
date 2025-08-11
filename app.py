import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Read secret key from environment (Render → Environment Variables)
app.secret_key = os.environ.get("SECRET_KEY", "dev-fallback-key")

# Read FLASK_ENV from environment (optional, default: development)
flask_env = os.environ.get("FLASK_ENV", "development")

# Debug info (only in non-production mode)
if flask_env != "production":
    print("SECRET_KEY length:", len(app.secret_key))
    print("FLASK_ENV:", flask_env)

@app.route("/")
def home():
    return "Flask app is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    product = data.get("product")
    time = data.get("time")

    # Example dummy logic
    if "salicylic acid" in product.lower() and "retinol" in product.lower():
        return jsonify({"warning": "Avoid using salicylic acid with retinol together"})
    else:
        return jsonify({"message": f"Safe to use in {time}"})

    

    if request.method == "POST":
        try:
            data = request.get_json()

            product = data.get("product", "").lower()
            time = data.get("time", "").lower()

            if "salicylic acid" in product and "retinol" in product:
                result = "Avoid using salicylic acid and retinol together. Use one in the morning and the other at night."
            elif "salicylic acid" in product:
                result = "Best used in the morning with sunscreen."
            elif "retinol" in product:
                result = "Best used at night to avoid sun sensitivity."
            else:
                result = "No special restrictions for this ingredient."

            return jsonify({
                "product": product,
                "time": time,
                "advice": result
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


    
