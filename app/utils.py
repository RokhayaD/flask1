from flasgger import Swagger
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Initialisation de Swagger
    swagger = Swagger(app)

    # Configuration de votre application ici

    return app
