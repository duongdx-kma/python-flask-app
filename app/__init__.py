from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Create an instance of SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize the SQLAlchemy instance
    db.init_app(app)

    # Import routes inside the app context to avoid circular imports
    with app.app_context():
        from app.routers import register_routes  # Import routes here after db initialization
        register_routes(app)

    return app
