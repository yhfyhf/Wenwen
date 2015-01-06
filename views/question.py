# encoding: utf-8
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


@app.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'POST':
        title       = request.form['title'].strip()
        description = request.form['description'].strip()

        if not title:
            flash(u'Please write down your question!', 'error')
        else:
            question = Question(title, description, g.user.id)
            db.session.add(question)
            db.session.commit()
            flash(u'Question published!')
            return redirect(url_for('index'))
    return render_template('question.html')

@app.route('/questions/<int:question_id>', methods=['GET' , 'POST'])
@login_required
def show_or_update(question_id):
    question = Question.query.get(question_id)
    if not question:
        flash(u'Question not exist!', 'error')
        return redirect(url_for('index'))

    if request.method == 'GET':
        answers = Answer.query.filter_by(question_id=question_id).all()
        return render_template('view.html', question=question, answers=answers)

    # request method is POST
    if question.user_id == g.user.id:   
        title = request.form['title'].strip()
        if not title:
            flash(u'Please write down your question!', 'error')
        else:
            question.title        = title
            question.description  = request.form['description'].strip()
            db.session.commit()
            return redirect(url_for('index'))
    else:  # not this user's question
        flash(u'Permission denied.', 'error')
    return redirect(url_for('show_or_update', question_id=question.id))
