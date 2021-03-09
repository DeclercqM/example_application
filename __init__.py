import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from . import config

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate()

app.config.from_object(config.Config())

db.init_app(app)
migrate.init_app(app, db, os.path.join(basedir, 'migrations'))

from app import routes
