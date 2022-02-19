import os

class Config(object):
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.dirname(__file__)
    DATABASE = os.path.join(BASE_DIR, "app/main.db")
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jdlfjds7834kjfksdfhdsds'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
