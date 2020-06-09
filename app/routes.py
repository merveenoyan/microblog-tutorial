from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Merve'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }

    ]
    return render_template("index.html", title="Home", user=user, posts=posts)

#The routes are the different URLs that the application implements.
#In Flask, handlers for the application routes are written as Python functions, called view functions.
#View functions are mapped to one or more route URLs so that Flask knows what 
# logic to execute when a client requests a given URL.
# the @app.route decorator creates an association between 
# the URL given as an argument and the function. 
# In this example there are two decorators, which associate the URLs / and /index to this function. 
# This means that when a web browser requests either of these two URLs, Flask is going to invoke this function and 
# pass the return value of it back to the browser as a response. 
# The operation that converts a template into a complete HTML page is called rendering. 
# To render the template I had to import a function that comes with the Flask framework called render_template(). This function takes a template filename and a variable list of template arguments and returns the same template, 
# but with all the placeholders in it replaced with actual values.