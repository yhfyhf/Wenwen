from flask import request
from mysite.model.user import User
from mysite.api import api, CONTENTTYPE
from mysite.api.const import Error
from mysite.api.utils.render import ok, error


@api.route('/account/login', methods=['POST'])
def login():
	username = request.form.get('username', '').strip()
	password = request.form.get('password', '').strip()

	if not username:
		return error(Error.user_username_empty)
	if not password:
		return error(Error.user_password_empty)

	user = User.query.filter_by(username=username).first()

	if not user:
		return error(Error.user_not_exist)
	if not user.check_password(password):
		return error(Error.user_wrong_password)

	ret = user.to_dict()
	ret.pop("password")
	return ok(ret), 200, CONTENTTYPE
