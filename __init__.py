from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import *
from OpenSSL import SSL


context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('host.key')
context.use_certificate_file('host.crt')

app = Flask(__name__)
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secret_key'
app.config['DEBUG'] = False    # Flask-sslify only works when DEBUG is False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_HOST_ONLINE
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)

from mysite.views import index   # must import after app generated
from mysite.views import login
from mysite.views import logout
from mysite.views import new
from mysite.views import register
from mysite.views import question

from mysite.api import api
app.register_module(api, url_prefix="/api")
