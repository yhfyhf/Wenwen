# encoding: utf-8
from flask import request, render_template, flash, redirect, url_for
from flask.ext.login import login_user
from mysite import app
from mysite.model.user import User
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


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
        flash(u'用户名不存在！' , 'error')
        return redirect(url_for('login'))
    if not registered_user.check_password(password):
        flash(u'密码错误！','error')
        return redirect(url_for('login'))
    login_user(registered_user, remember=remember_me)
    flash(u'登录成功！')
    return redirect(request.args.get('next') or url_for('index'))
