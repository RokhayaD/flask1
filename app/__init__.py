from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


SWAGGER_URL = '/swagger'


API_URL = '/static/swagger.json' 
def create_app():
    app = Flask(__name__)
    
    #
    app.config.from_object(Config)

   
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "My API"}  
    )

   
    db.init_app(app)
    migrate.init_app(app, db)

    
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)  
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)  

    return app
