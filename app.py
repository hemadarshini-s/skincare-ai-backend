import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret key from environment
app.secret_key = os.environ.get("SECRET_KEY", "dev-fallback-key")
flask_env = os.environ.get("FLASK_ENV", "development")

if flask_env != "production":
    print("SECRET_KEY length:", len(app.secret_key))
    print("FLASK_ENV:", flask_env)

@app.route("/")
def home():
    return "Flask app is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        product = data.get("product", "").lower()
        time = data.get("time", "").lower()

        warnings = []
        recommendations = []
        note = ""

        # Rules
        if "salicylic acid" in product and "retinol" in product:
            warnings.append("Avoid using salicylic acid and retinol together.")
            recommendations.append("Use salicylic acid in the morning with sunscreen.")
            recommendations.append("Use retinol at night to avoid sun sensitivity.")
            note = "Both are strong actives and can cause irritation if combined."
        elif "salicylic acid" in product:
            recommendations.append("Best used in the morning with sunscreen.")
            note = "Salicylic acid exfoliates and can increase sun sensitivity."
        elif "retinol" in product:
            recommendations.append("Best used at night.")
            note = "Retinol can cause photosensitivity and works better overnight."
        else:
            recommendations.append(f"Safe to use in the {time}.")
            note = "No major restrictions detected for these ingredients."

        return jsonify({
            "product": product,
            "time": time,
            "warnings": warnings,
            "recommendations": recommendations,
            "note": note
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

