from flask import (
    Flask,
    render_template,
    session,
    request,
    Blueprint,
    redirect,
    url_for,
    flash,
)
from passlib.hash import sha256_crypt
import QUERYDB as db


# app = Flask(__name__, template_folder="templates", static_url_path="/static")
login_blueprint = Blueprint("login_page", __name__)
logout_blueprint = Blueprint("logout_page", __name__)


@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        password_candidate = request.form['password']
        print(password_candidate)
        checkPlease = sha256_crypt.encrypt(str(password_candidate))
        print(checkPlease)
        print('this is the password')
        cur = db.db.cursor()
        results = cur.execute('SELECT * from users where username = %s' , [username])
        print('complete')
        if results > 0:
            print('hello again')
            data = cur.fetchone()
            password = data[4]
            print(password)
            confirmed = data[5]
            fullname = data[3]
            user_id = data[0]
            if confirmed == 0:
                error = 'Please confirm email before logging in'
                return render_template('login.html', error=error)
            elif sha256_crypt.verify(password_candidate, password) and user_id < 9000001:
                session['logged_in'] = True
                session['user_id'] = user_id
                session['username'] = username
                session['fullname'] = fullname
                return redirect(url_for('studDash'))
            elif sha256_crypt.verify(password_candidate, password) and user_id > 9000000:
                session['logged_in'] = True
                session['user_id'] = user_id
                session['username'] = username
                session['fullname'] = fullname
                return redirect(url_for('teachDash'))  
            else:
                error = 'Invalid password'
                return render_template('login.html', error=error)
                cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
    return render_template('login.html')

@logout_blueprint.route('/logout')
def logout():
	session.clear()
	flash('Successfully logged out', 'success')
	return redirect(url_for('index'))