import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://rokhaya:Passer123@localhost/flask_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
