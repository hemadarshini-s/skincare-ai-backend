if flask_env != "production":
    # Only show in non-production mode
    print("SECRET_KEY length:", len(app.secret_key))
    print("FLASK_ENV:", flask_env)
