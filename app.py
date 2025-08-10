import os
from flask import Flask

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

if __name__ == "__main__":
    # Default to 0.0.0.0 for Render
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
