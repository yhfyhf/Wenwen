# encoding: utf-8
from flask import request, flash, g, redirect, url_for, render_template
from flask.ext.login import login_required
from mysite import app, db
from mysite.model.question import Question
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        if not request.form['title']:
            flash(u'Please write down your questions!', 'error')
        else:
            question = Question(request.form['title'], request.form['description'], g.user.id)
            db.session.add(question)
            db.session.commit()
            flash(u'Question published!')
            return redirect(url_for('index'))
    return render_template('new.html')
    