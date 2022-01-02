from flask import (
    Flask,
    render_template,
    session,
    request,
    Blueprint,
    redirect,
    url_for,
)
from passlib.hash import sha256_crypt
import db


app = Flask(__name__, template_folder="templates", static_url_path="/static")
login_blueprint = Blueprint("login_page", __name__)


@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        cur = db.db.cursor()
        results = cur.execute('SELECT * from users where username = %s' , [username])
        if results > 0:
            data = cur.fetchone()
            password = data['password']
            confirmed = data['confirmed']
            fullname = data['fullname']
            user_id = data['user_id']
            if confirmed == 0:
                error = 'Please confirm email before logging in'
                return render_template('login.html', error=error)
            elif sha256_crypt.verify(password_candidate, password) and user_id < 9000001:
                session['logged_in'] = True
                session['username'] = username
                session['fullname'] = fullname
                return redirect(url_for('studDash.html'))
            elif sha256_crypt.verify(password_candidate, password) and user_id > 9000000:
                session['logged_in'] = True
                session['username'] = username
                session['fullname'] = fullname
                return redirect(url_for('teachDash.html'))
                ##may need to add if statement for redirect here for teacher.  
            else:
                error = 'Invalid password'
                return render_template('login', error=error)
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
    return render_template('login.html')