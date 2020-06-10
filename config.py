import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///'+ os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# Flask sqlalchemy uzantisi database'in konumunu sqlalchemy_database_uri'dan alir

# Flask and some of its extensions use the value of the secret key as a cryptographic key, useful to generate signatures or tokens. 
#The Flask-WTF extension uses it to protect web forms against a nasty attack called Cross-Site Request Forgery or CSRF (pronounced "seasurf"). 