from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register routes inside the function to avoid circular imports
    with app.app_context():
        from . import routes

    return app