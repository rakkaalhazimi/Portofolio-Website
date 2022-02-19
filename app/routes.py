import os, sys
import platform
import datetime as dt
from flask import (
    render_template,
    url_for,
    redirect,
    request,
    make_response,
    abort,
    jsonify,
    session,
    flash)
from app import app
from app.helpers import *
from app.forms import *
from app.models import *

# Home route
@app.route('/')
def index():
    return render_template('index.html', projects=Projects.query.all())

@app.route('/platform')
def get_platform_name():
    return platform.system()

@app.route('/env')
def get_env():
    return app.config["ENV"]

@app.route('/projects')
def get_project():
    return Projects.query.all()[0].title