# encoding: utf-8
from flask import Blueprint

CONTENTTYPE = {"Content-Type": "application/json; charset=utf-8"}

api = Blueprint('api', __name__)

import mysite.api.utils.verify_password
import mysite.api.views.question
import mysite.api.views.account
