from flask import (
    Flask,
    render_template,
    render_template_string,
    request,
    Blueprint,
    flash,
    redirect,
    url_for,
)
import db
from classes import RegisterForm
from random import randint
from passlib.hash import sha256_crypt
from flask_mail import Mail, Message
from emailverifier import Client
from itsdangerous import URLSafeTimedSerializer
import os, config

registration_blueprint = Blueprint("registration", __name__)

app = Flask(__name__, template_folder="templates", static_url_path="/static")
app.config.from_object(os.environ.get('config.DevelopementConfig'))

client = Client("at_rFxZz7zEX8CO8V5IDBfzexOe2fW8b")


htmlbody = """
Your account on <b>The Best</b> Quiz App was successfully created.
Please click the link below to confirm your email address and
activate your account:
  
<a href="{{ confirm_url }}">{{ confirm_url }}</a>
 <p>
--
Questions? Comments? Email </p>
"""

@registration_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        fullname = form.name.data
        email = form.email.data
        teachercode = form.teachercode.data
        
        data = client.get(email) 
        if str(data.smtp_check) == 'False': 
            flash('Invalid email, please provide a valid email address','danger')
            return render_template('register.html', form=form)
            
        send_confirmation_email(email) 
        user_id = randint(0,900000)
        if teachercode == "KURATEACH2022":
            user_id = randint(900000,999999)
        print(user_id)
        
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        cur = db.db.cursor()
        cur.execute(
            "INSERT INTO users(user_id, username,fullname,email, password,confirmed) values(%s,%s,%s,%s,%s,0)",
            (user_id, username, fullname, email, password),
        )
        db.db.commit()
        cur.close()
        flash(
            "Thanks for registering!  Please check your email to confirm your email address.",
            "success",
        )
        return redirect(url_for("login"))
        # change in login function to redirect to warning page

    return render_template("register.html", form=form)

def send_email(recipients, html_body):
    try:
        msg = Message(
            "Confirm Your Email Address",
            sender="nycazn724@gmail.com",
            recipients=recipients,
        )
        msg.html = html_body
        send_async_email(app, msg)
        # return 'Mail sent!'
        return
    except Exception as e:
        # return(str(e))
        return


# def get_local_ip():
# 	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 	s.connect(('8.8.8.8', 1))
# 	local_ip_address = s.getsockname()[0]
# 	return local_ip_address

"""This here will grab the address of the host where it is hosting to create to be used in a url later on. IPBased commented out for now"""

# @asynch   ##unclear of this is needed since the function is invoked in app.py
# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)

def send_confirmation_email(user_email):
    confirm_serializer = URLSafeTimedSerializer(config.BaseConfig.SECRET_KEY)
    print(user_email)
    print(confirm_serializer.dumps(user_email, salt="email-confirmation-salt"))
    ##https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask
    confirm_url = url_for(
        "registration.confirm_email",
        token=confirm_serializer.dumps(user_email, salt="email-confirmation-salt"),
        _external=True,
    )
    print(confirm_url)
    local_ip = "127.0.0.1"  # "get_local_ip() changed for testing
    x = ""
    if "localhost" in confirm_url:
        x = confirm_url.split("localhost:5000")
    else:
        x = confirm_url.split("127.0.0.1:5000")
    confirm_url = x[0] + local_ip + ":5000" + x[1]
    html = render_template_string(htmlbody, confirm_url=confirm_url)

    send_email([user_email], html)

# """This here salts the secret key and creates a token based off the user email added to secret key"""


@registration_blueprint.route("/confirm/<token>")
def confirm_email(token):
    try:
        confirm_serializer = URLSafeTimedSerializer(config.BaseConfig.SECRET_KEY)
        email = confirm_serializer.loads(
            token, salt="email-confirmation-salt", max_age=3600
        )
    except:
        flash("The confirmation link is invalid or has expired.", "error")
        return redirect(url_for("login"))

    cur = db.db.cursor()
    results = cur.execute("SELECT * from users where email = %s", [email])
    if results > 0:
        data = cur.fetchone()
        email_confirmed = data[5]
        if email_confirmed:
            flash("Account already confirmed. Please login.", "info")
        else:
            results = cur.execute(
                "UPDATE users SET confirmed = 1 where email = %s", [email]
            )
            db.db.commit()
            cur.close()
            flash("Thank you for confirming your email address!", "success")
            return redirect(url_for("login"))
        return redirect(url_for("index"))


"""This here salts the secret key and creates a token based off the user email added to secret key"""
