from flask import Module


CONTENTTYPE = {"Content-Type": "application/json; charset=utf-8"}

api = Module(__name__)

from mysite.api.question import questions
