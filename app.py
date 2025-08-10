import os
from flask import Flask

app = Flask(__name__)

# Read secret key from environment
app.secret_key = os.environ.get("SECRET_KEY", "dev-fallback-key")

# Read FLASK_ENV from environment (optional)
flask_env = os.environ.get("FLASK_ENV", "development")
