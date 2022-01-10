# from _typeshed import HasFileno
from flask import (
    Flask,
    request,
    render_template,
    render_template_string,
    flash,
    redirect,
    url_for,
    session,
)
from flask_mail import Mail, Message
from flask_mysqldb import MySQL

import QUERYDB as db
import SQLCRUD as crud
import db
from upload_test import upload_test_blueprint
from serve_quiz import serve_quiz_blueprint

# from registration import registration_blueprint
from login import login_blueprint, logout_blueprint
from results import results_blueprint
from functools import wraps
from threading import Thread

# import socket
import os, config
from itsdangerous import URLSafeTimedSerializer
from emailverifier import Client
from passlib.hash import sha256_crypt
from random import randint
from classes import RegisterForm
from sessioncheck import is_logged

from datetime import timedelta, datetime


app = Flask(__name__, template_folder="templates", static_url_path="/static")
app.config.from_object(os.environ.get("FLASK_ENV") or "config.DevelopementConfig")
app.register_blueprint(upload_test_blueprint)
app.register_blueprint(serve_quiz_blueprint)
app.register_blueprint(results_blueprint)


# app.register_blueprint(registration_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)

mail = Mail(app)


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


# def is_logged(f):
# 	@wraps(f)
# 	def wrap(*args, **kwargs):
# 		if 'logged_in' in session:
# 			return f(*args, **kwargs)
# 		else:
# 			flash('Unauthorized, Please login','danger')
# 			return redirect(url_for('login_page.login'))
# 	return wrap


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/studDash", methods=["GET", "POST"])
@is_logged
def studDash():
    return render_template("studDash.html")


@app.route("/quiz2")
def quiz2():
    data = db.grab_question2("quiz1")
    crud.insert_session(22222, "quiz1")

    i = 0  # q1
    question_prompt1 = data.get("question")[i]
    option_1a = data.get("choices")[i][0]
    option_1b = data.get("choices")[i][1]
    option_1c = data.get("choices")[i][2]
    option_1d = data.get("choices")[i][3]
    i += 1  # q2
    question_prompt2 = data.get("question")[i]
    option_2a = data.get("choices")[i][0]
    option_2b = data.get("choices")[i][1]
    option_2c = data.get("choices")[i][2]
    option_2d = data.get("choices")[i][3]
    i += 1  # q3
    question_prompt3 = data.get("question")[i]
    option_3a = data.get("choices")[i][0]
    option_3b = data.get("choices")[i][1]
    option_3c = data.get("choices")[i][2]
    option_3d = data.get("choices")[i][3]
    i += 1  # q4
    question_prompt4 = data.get("question")[i]
    option_4a = data.get("choices")[i][0]
    option_4b = data.get("choices")[i][1]
    option_4c = data.get("choices")[i][2]
    option_4d = data.get("choices")[i][3]
    i += 1  # q5
    question_prompt5 = data.get("question")[i]
    option_5a = data.get("choices")[i][0]
    option_5b = data.get("choices")[i][1]
    option_5c = data.get("choices")[i][2]
    option_5d = data.get("choices")[i][3]
    i += 1  # q6
    question_prompt6 = data.get("question")[i]
    option_6a = data.get("choices")[i][0]
    option_6b = data.get("choices")[i][1]
    option_6c = data.get("choices")[i][2]
    option_6d = data.get("choices")[i][3]
    i += 1  # q7
    question_prompt7 = data.get("question")[i]
    option_7a = data.get("choices")[i][0]
    option_7b = data.get("choices")[i][1]
    option_7c = data.get("choices")[i][2]
    option_7d = data.get("choices")[i][3]
    i += 1  # q8
    question_prompt8 = data.get("question")[i]
    option_8a = data.get("choices")[i][0]
    option_8b = data.get("choices")[i][1]
    option_8c = data.get("choices")[i][2]
    option_8d = data.get("choices")[i][3]
    i += 1  # q9
    question_prompt9 = data.get("question")[i]
    option_9a = data.get("choices")[i][0]
    option_9b = data.get("choices")[i][1]
    option_9c = data.get("choices")[i][2]
    option_9d = data.get("choices")[i][3]
    i += 1  # q10
    question_prompt10 = data.get("question")[i]
    option_10a = data.get("choices")[i][0]
    option_10b = data.get("choices")[i][1]
    option_10c = data.get("choices")[i][2]
    option_10d = data.get("choices")[i][3]

    return render_template(
        "quiz-2.html",
        question_prompt1="1. " + question_prompt1,
        option_1a=option_1a,
        option_1b=option_1b,
        option_1c=option_1c,
        option_1d=option_1d,
        question_prompt2="2. " + question_prompt2,
        option_2a=option_2a,
        option_2b=option_2b,
        option_2c=option_2c,
        option_2d=option_2d,
        question_prompt3="3. " + question_prompt3,
        option_3a=option_3a,
        option_3b=option_3b,
        option_3c=option_3c,
        option_3d=option_3d,
        question_prompt4="4. " + question_prompt4,
        option_4a=option_4a,
        option_4b=option_4b,
        option_4c=option_4c,
        option_4d=option_4d,
        question_prompt5="5. " + question_prompt5,
        option_5a=option_5a,
        option_5b=option_5b,
        option_5c=option_5c,
        option_5d=option_5d,
        question_prompt6="6. " + question_prompt6,
        option_6a=option_6a,
        option_6b=option_6b,
        option_6c=option_6c,
        option_6d=option_6d,
        question_prompt7="7. " + question_prompt7,
        option_7a=option_7a,
        option_7b=option_7b,
        option_7c=option_7c,
        option_7d=option_7d,
        question_prompt8="8. " + question_prompt8,
        option_8a=option_8a,
        option_8b=option_8b,
        option_8c=option_8c,
        option_8d=option_8d,
        question_prompt9="9. " + question_prompt9,
        option_9a=option_9a,
        option_9b=option_9b,
        option_9c=option_9c,
        option_9d=option_9d,
        question_prompt10="10. " + question_prompt10,
        option_10a=option_10a,
        option_10b=option_10b,
        option_10c=option_10c,
        option_10d=option_10d,
    )


# @app.route("/results")
# def results():
#     quiz = "quiz1"
#     session_id = 123456
#     max_question = 10
#     total_score = 0
#     db.update_total_score(session_id, quiz, total_score)

#     for number in range(1, max_question + 1):
#         # question_number = number
#         # question_prompt = db.query_question(quiz, number)[0]
#         user_answer = str(db.get_user_answer(session_id, quiz, number)).strip()
#         actual_answer = str(db.get_actual_answer(quiz, number)).strip()

#         if user_answer == actual_answer:
#             total_score += 1
#             db.update_total_score(session_id, quiz, total_score)
#         else:
#             print(f"{number} is incorrect!")

#     return render_template("tests_result.html", total_score=total_score)


# Barebones for API Calls
# refs
# https://pythonbasics.org/flask-http-methods/
# https://stackoverflow.com/questions/40963401/flask-dynamic-data-update-without-reload-page/40964086


## This list all the tables inside the database final
# print(f"Original List: {db.list_tables(db_table = 'final')}\n")

## This creates a table named <var>
# db.create_table(new_name="testing_purpose")
# print(f"New List: {db.list_tables(db_table = 'final')}\n")

## This deletes a table named <var>
# db.delete_table(target="testing_purpose")
# print(f"New List: {db.list_tables(db_table = 'final')}\n")


def asynch(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


@asynch
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


client = Client("at_zmz5m4BQ9kegkMqfGaTujPCCUD135")  ##whoisxmlapikey


htmlbody = """
Your account on <b>QuizNose</b> Quiz App was successfully created.
Please click the link below to confirm your email address and
activate your account:
  
<a href="{{ confirm_url }}">{{ confirm_url }}</a>
 <p>
--
Questions? Comments? Email </p>
"""


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        cur = db.db.cursor()
        fullname = form.name.data
        username = form.username.data
        checkUsername = cur.execute('SELECT * from users where username = %s' , [fullname])
        usernameDataLength = len(cur.fetchall())
        if usernameDataLength > 0:
            flash("This username has already been taken, please choose another", "danger")
            return render_template("register.html", form = form)
        email = form.email.data
        checkEmailAddress = cur.execute('SELECT * from users where email = %s' , [email])
        emailDataLength = len(cur.fetchall())
        if emailDataLength > 0:
            flash("This email has already registered an account, please choose another", "danger")
            return render_template("register.html", form = form)
        teachercode = form.teachercode.data
        user_id = randint(0, 900000)
        checkUserID = cur.execute('SELECT * from users where user_id = %s' , [user_id])
        userIDDataLength = len(cur.fetchall())
        while userIDDataLength == 1:
            user_id = randint(0, 900000)
            return user_id
        ##code here add to check of that random value already present in db
        # if so, reroll
        if teachercode == "KURATEACH2022":
            user_id = randint(900000, 999999)
            checkUserID = cur.execute('SELECT * from users where user_id = %s' , [user_id])
            userIDDataLength = len(cur.fetchall())
            while userIDDataLength == 1:
                user_id = randint(0, 900000)
                return user_id
        print(user_id)
        ##same process here.

        data = client.get(email)
        if str(data.smtp_check) == "False":
            flash("Invalid email, please provide a valid email address", "danger")
            return render_template("register.html", form = form)


        send_confirmation_email(email)

        password = sha256_crypt.encrypt(str(form.password.data))
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
        return redirect(url_for("login_page.login"))
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


def send_confirmation_email(user_email):
    confirm_serializer = URLSafeTimedSerializer(config.DevelopementConfig.SECRET_KEY)
    print(user_email)
    print(confirm_serializer.dumps(user_email, salt="email-confirmation-salt"))
    ##https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask
    confirm_url = url_for(
        "confirm_email",
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


@app.route("/confirm/<token>")
def confirm_email(token):
    try:
        confirm_serializer = URLSafeTimedSerializer(
            config.DevelopementConfig.SECRET_KEY
        )
        email = confirm_serializer.loads(
            token, salt="email-confirmation-salt", max_age=3600
        )
    except:
        flash("The confirmation link is invalid or has expired.", "error")
        return redirect(url_for("login_page.login"))

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
            return redirect(url_for("login_page.login"))
        return redirect(url_for("index"))


"""This here salts the secret key and creates a token based off the user email added to secret key"""

if __name__ == "__main__":
    app.run(host="0.0.0.0")
