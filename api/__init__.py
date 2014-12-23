# encoding: utf-8
from flask import Blueprint

CONTENTTYPE = {"Content-Type": "application/json; charset=utf-8"}

api = Blueprint('api', __name__)

import mysite.api.verify_password
from mysite.api.question import questions
import mysite.api.account
