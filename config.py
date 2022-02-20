import os
base_dir = os.path.dirname(__file__)

class Config(object):
    DEBUG = False
    TESTING = False

    RESUME_PATH = os.path.join(base_dir, "app/static/download/Resume-PythonDeveloper.pdf")

    DATABASE = os.path.join(base_dir, "app/main.db")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@ec2-54-209-221-231.compute-1.amazonaws.com:5432/dd6qv5s1bur2gf'.format(os.environ["POSGRES_USERNAME"], os.environ["POSGRES_PASSWORD"])
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jdlfjds7834kjfksdfhdsds'
    

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
