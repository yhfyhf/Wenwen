# encoding: utf-8
from flask import request, render_template, flash, redirect, url_for
from mysite import app, db
from mysite.model.user import User
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    # request method is POST
    session = db.session     
    un = request.form['username']
    e = request.form['email']

    all_usernames = session.query(User.username).all()
    all_emails = session.query(User.email).all()
    
    if (un,) in all_usernames:   # username existed
        flash(u"用户名已被注册！")
        session.close()
        return redirect(url_for('register'))
    if (e,) in all_emails:       # email existed
        flash(u"邮箱已被注册！")
        session.close()
        return redirect(url_for('register'))

    else:
        user = User(un, request.form['password'], e)
        session.add(user)
        session.commit()
        session.close()
        flash(u'注册成功！')
        return redirect(url_for('login'))
