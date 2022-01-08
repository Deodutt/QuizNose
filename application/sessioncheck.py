from flask import (
	Flask,
    session,
    redirect,
    url_for,
    flash,
)
from functools import wraps

# app = Flask(__name__, template_folder="templates", static_url_path="/static")


def is_logged(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorized, Please login','danger')
			return redirect(url_for('login_page.login'))
	return wrap

