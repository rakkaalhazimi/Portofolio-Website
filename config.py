import os
base_dir = os.path.dirname(__file__)

class Config(object):
    DEBUG = False
    TESTING = False

    RESUME_PATH = os.path.join(base_dir, "app/static/download/Resume-PythonDeveloper.pdf")

    DATABASE = os.path.join(base_dir, "app/main.db")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}'.format(os.environ["POSGRES_USERNAME"], os.environ["POSGRES_PASSWORD"], os.environ["POSGRES_SERVER"])
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jdlfjds7834kjfksdfhdsds'
    

class ProductionConfig(Config):
    ...

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
