from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import *


app = Flask(__name__)
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secret_key'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DB_HOST_ONLINE

db = SQLAlchemy(app)

from mysite.views import index   # must import after app generated
from mysite.views import login
from mysite.views import logout
from mysite.views import new
from mysite.views import register
from mysite.views import question
