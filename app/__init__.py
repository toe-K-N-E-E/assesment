from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask( __name__ )

app.config[ "SQLALCHEMY_DATABASE_URI" ] = "sqlite:///" + os.path.join( basedir, "messages.db" )
app.config[ "SQLALCHEMY_TRACK_MODIFICATIONS" ] = False

db = SQLAlchemy( app )
migrate = Migrate( app, db )

from app import routes, models
