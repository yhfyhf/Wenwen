#encoding: utf-8
from flask import render_template, request, g, redirect, url_for, flash
from flask.ext.login import login_required
from mysite import app, db
from mysite.model.question import Question
from mysite.model.answer import Answer
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


@app.route('/answer/<int:question_id>', methods = ['GET' , 'POST'])
@login_required
	if request.mothod == "POST":
		if not request.form['content'].strip:
