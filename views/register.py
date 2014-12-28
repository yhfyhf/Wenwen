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
    pw = request.form['password']
    if not un or not pw:
        print "None" 
        flash(u"Please input your username and password!")
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
