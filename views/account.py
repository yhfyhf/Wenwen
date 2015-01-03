# encoding: utf-8
from flask import request, render_template, flash, redirect, url_for
from flask.ext.login import login_user, logout_user
from mysite import app, db
from mysite.model.user import User
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    # request method is POST
    session = db.session     
    un = request.form['username']
    pw = request.form['password']
    if not un or not pw:
        print "None" 
        flash(u"Please input your username and password!", "error")
        session.close()
        return redirect(url_for('register'))

    all_usernames = session.query(User.username).all()
    
    if (un,) in all_usernames:   # username existed
        flash(u"Username existed!")
        session.close()
        return redirect(url_for('register'))
    else:
        user = User(un, pw)
        session.add(user)
        session.commit()
        session.close()
        flash(u'Register successfully')
        return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # request method is POST
    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = User.query.filter_by(username=username).first()
    if registered_user is None:
        flash(u'Username not exists!', 'error')
        return redirect(url_for('login'))
    if not registered_user.check_password(password):
        flash(u'Wrong password!', 'error')
        return redirect(url_for('login'))
    login_user(registered_user, remember=remember_me)
    flash(u'Login successfully!')
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
