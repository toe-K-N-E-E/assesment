from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask( __name__ )

app.config[ "SQLALCHEMY_DATABASE_URI" ] = "sqlite:///{}".format(os.path.join(os.path.abspath(os.path.dirname(__file__)), "messages.db"))
app.config[ "SQLALCHEMY_TRACK_MODIFICATIONS" ] = False

db = SQLAlchemy( app )

from app import routes
