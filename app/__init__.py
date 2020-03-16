from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask( __name__ )

#comment this out if not using SQLite
app.config[ "SQLALCHEMY_DATABASE_URI" ] = "sqlite:///" + os.path.join( basedir, "messages.db" )

#use this for MYSQL db
#app.config[ "SQLALCHEMY_DATABASE_URI" ] = "mysql://{username}:{password}@{hostname}/{databasename}".format( username="SET USERNAME HERE", password="SET PASSWORD HERE",
#                                                                                                             hostname="SET HOSTNAME HERE", databasename="SET HOSTNAME HERE" )
app.config[ "SQLALCHEMY_TRACK_MODIFICATIONS" ] = False

db = SQLAlchemy( app )
migrate = Migrate( app, db )

from app import routes, models
