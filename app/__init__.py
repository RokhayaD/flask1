from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

# URL pour accéder à l'interface Swagger
SWAGGER_URL = '/swagger'

# Chemin vers votre fichier swagger.json
API_URL = '/static/swagger.json'  # Assurez-vous que ce fichier existe bien dans le dossier 'static'

def create_app():
    app = Flask(__name__)
    
    # Charger la configuration depuis un objet de configuration (config.py)
    app.config.from_object(Config)

    # Initialisation de Swagger UI
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "My API"}  # Remplacez par le nom de votre application
    )

    # Initialisation de SQLAlchemy, Migrate et Marshmallow
    db.init_app(app)
    migrate.init_app(app, db)

    # Enregistrement des Blueprints
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)  # Enregistrement des routes principales
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)  # Enregistrement du blueprint Swagger

    return app
