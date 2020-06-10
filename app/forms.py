from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# The HTML <form> element is used as a container for the web form. 
# The action attribute of the form is used to tell the browser the URL that should be
#  used when submitting the information the user entered in the form.
#  The method attribute specifies the HTTP request method that should be used when submitting the form to the server. 
# The default is to send it with a GET request, but in almost all cases, using a POST request makes for a better user experience because requests of this type can submit the form data in the body of the request, 
# while GET requests add the form fields to the URL, cluttering the browser address bar.
#  The novalidate attribute is used to tell the web browser to not apply validation to the fields in this form, which effectively leaves this task to the Flask application running in the server.
#  Using novalidate is entirely optional, but for this first form it is important that you set it because this will allow you to test server-side validation later in this chapter.
# The form.hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks. 