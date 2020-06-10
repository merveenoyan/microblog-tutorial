from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import routes

# Flask uses the location of the module passed here as 
# a starting point when it needs to load associated resources such as template files

# For all practical purposes, passing __name__ is almost always going to configure Flask in the correct way. 
# The application then imports the routes module, which doesn't exist yet.

# db database'i temsil  ediyor,  migrate migration engine'i