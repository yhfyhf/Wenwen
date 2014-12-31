# encoding: utf-8
from flask import render_template, request, g, redirect, url_for, flash
from flask.ext.login import login_required
from mysite import app, db
from mysite.model.question import Question
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


@app.route('/questions/<int:question_id>', methods = ['GET' , 'POST'])
@login_required
def show_or_update(question_id):
    question = Question.query.get(question_id)
    if request.method == 'GET':
        return render_template('view.html', question=question)
    if question.user_id == g.user.id:
        question.title = request.form['title']
        question.description  = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    flash(u'Permission denied.','error')
    return redirect(url_for('show_or_update', question_id=question.id))

@app.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'POST':
        if not request.form['title']:
            flash(u'Please write down your questions!', 'error')
        else:
            question = Question(request.form['title'], request.form['description'], g.user.id)
            db.session.add(question)
            db.session.commit()
            flash(u'Question published!')
            return redirect(url_for('index'))
    return render_template('question.html')
