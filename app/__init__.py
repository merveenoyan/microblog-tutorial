from flask import Flask

app = Flask(__name__)

from app import routes

# Flask uses the location of the module passed here as 
# a starting point when it needs to load associated resources such as template files

# For all practical purposes, passing __name__ is almost always going to configure Flask in the correct way. 
# The application then imports the routes module, which doesn't exist yet.