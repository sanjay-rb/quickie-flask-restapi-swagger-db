# Importing flask modules to start with
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# create the extension
db = SQLAlchemy()

# Creating new flask app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
db_path = os.path.join(os.getcwd(), 'linky_with_sqlalchemy_app/linky.db')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(db_path)
# initialize the app with the extension
db.init_app(app)

from app import routes