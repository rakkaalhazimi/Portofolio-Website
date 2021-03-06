import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import configuration profile based on FLASK_ENV variable - defaults to Production
if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object('config.DevelopmentConfig')
elif os.environ.get('FLASK_ENV') == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.ProductionConfig')

# Import routes here
from app.routes import *