# Importing flask modules to start with
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# create the extension
db = SQLAlchemy()

# Creating new flask app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
db_path = os.path.join(os.getcwd(), 'one_to_many_relationship_db_app/linky.db')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + str(db_path)
# initialize the app with the extension
db.init_app(app)

from project import models

# To create db & table if not exsist
with app.app_context():
    db.create_all()

from project import routes