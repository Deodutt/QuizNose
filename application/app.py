# from _typeshed import HasFileno
from flask import (
    Flask,
    request,
    render_template,
    # flash,
    redirect,
    url_for,
    # session,
)
from flask_mail import Mail
from flask_mysqldb import MySQL
import QUERYDB as db
from upload_test import upload_test_blueprint
from serve_quiz import serve_quiz_blueprint
from registration import registration_blueprint
from login import login_blueprint
# from passlib.hash import sha256_crypt
from functools import wraps
from threading import Thread
# import socket
import os, config

app = Flask(__name__, template_folder="templates", static_url_path="/static")
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
app.register_blueprint(upload_test_blueprint)
app.register_blueprint(serve_quiz_blueprint)
app.register_blueprint(registration_blueprint)
app.register_blueprint(login_blueprint)

mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password_candidate = request.form['password']
#         cur = db.db.cursor()
#         results = cur.execute('SELECT * from users where username = %s' , [username])
#         if results > 0:
#             data = cur.fetchone()
#             password = data['password']
#             confirmed = data['confirmed']
#             fullname = data['fullname']
#             user_id = data['user_id']
#             if confirmed == 0:
#                 error = 'Please confirm email before logging in'
#                 return render_template('login.html', error=error)
#             elif sha256_crypt.verify(password_candidate, password) and user_id < 9000001:
#                 session['logged_in'] = True
#                 session['username'] = username
#                 session['fullname'] = fullname
#                 return redirect(url_for('studDash'))
#             elif sha256_crypt.verify(password_candidate, password) and user_id > 9000000:
#                 session['logged_in'] = True
#                 session['username'] = username
#                 session['fullname'] = fullname
#                 return redirect(url_for('teachDash'))
#                 ##may need to add if statement for redirect here for teacher.  
#             else:
#                 error = 'Invalid password'
#                 return render_template('login.html', error=error)
#             cur.close()
#         else:
#             error = 'Username not found'
#             return render_template('login.html', error=error)
#     return render_template('login.html')


@app.route("/studDash")
def studDash():
    return render_template("studDash.html")


def display_question(quiz_id):
    global question_prompt, option_a, option_b, option_c, option_d

    max_questions = 10
    current_question = int(db.get_current_question(123456, quiz_id))
    if current_question < max_questions:
        data = db.serve_question(quiz_id, current_question)
        question_prompt = data.get("question")[0]
        option_a = data.get("choices")[0]
        option_b = data.get("choices")[1]
        option_c = data.get("choices")[2]
        option_d = data.get("choices")[3]
        return question_prompt, option_a, option_b, option_c, option_d
    else:
        print("finished test")
        return render_template("test_results.html")


def update_session(quiz_id, current_question, user_answer):
    current_question = int(db.get_current_question(123456, quiz_id))

    # inserting answer and updating current question
    db.insert_session_answer(
        123456,
        new_current_question,
        user_answer,
    )
    return


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    quiz = "quiz1"
    session = 123456
    max_questions = 10
    current_question = int(db.get_current_question(session, quiz))
    print(db.get_current_question(session, quiz))
    print(f"current question -> {current_question}")
    if current_question < max_questions:
        data = db.serve_question(quiz, current_question)
        question_prompt = data.get("question")[0]
        option_a = data.get("choices")[0]
        option_b = data.get("choices")[1]
        option_c = data.get("choices")[2]
        option_d = data.get("choices")[3]

        if request.method == "POST" and "choice_a" in request.form["quiz_choice"]:
            # update the question counter and record the answer user had
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            db.insert_session_answer(session, current_question, option_a)
            return render_template(
                "quiz.html",
                current_question=current_question,
                question_prompt=question_prompt,
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
            )

        elif request.method == "POST" and "choice_b" in request.form["quiz_choice"]:
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            db.insert_session_answer(session, current_question, option_a)
            return render_template(
                "quiz.html",
                current_question=current_question,
                question_prompt=question_prompt,
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
            )

        elif request.method == "POST" and "choice_c" in request.form["quiz_choice"]:
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            db.insert_session_answer(session, current_question, option_a)
            return render_template(
                "quiz.html",
                current_question=current_question,
                question_prompt=question_prompt,
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
            )

        elif request.method == "POST" and "choice_d" in request.form["quiz_choice"]:
            current_question = current_question + 1
            db.insert_session_counter(session, current_question)
            db.insert_session_answer(session, current_question, option_a)
            return render_template(
                "quiz.html",
                current_question=current_question,
                question_prompt=question_prompt,
                option_a=option_a,
                option_b=option_b,
                option_c=option_c,
                option_d=option_d,
            )
    else:
        print("finished test")
        return render_template("tests_result.html")

    return render_template(
        "quiz.html",
        current_question=current_question,
        question_prompt=question_prompt,
        option_a=option_a,
        option_b=option_b,
        option_c=option_c,
        option_d=option_d,
    )


@app.route("/quiz2")
def quiz2():
    data = db.grab_question2("quiz1")

    i=0 #q1
    question_prompt1 = data.get("question")[i]
    option_1a = data.get("choices")[i][0]
    option_1b = data.get("choices")[i][1]
    option_1c = data.get("choices")[i][2]
    option_1d = data.get("choices")[i][3]
    i+=1 #q2
    question_prompt2 = data.get("question")[i]
    option_2a = data.get("choices")[i][0]
    option_2b = data.get("choices")[i][1]
    option_2c = data.get("choices")[i][2]
    option_2d = data.get("choices")[i][3]
    i+=1 #q3
    question_prompt3 = data.get("question")[i]
    option_3a = data.get("choices")[i][0]
    option_3b = data.get("choices")[i][1]
    option_3c = data.get("choices")[i][2]
    option_3d = data.get("choices")[i][3]
    i+=1 #q4
    question_prompt4 = data.get("question")[i]
    option_4a = data.get("choices")[i][0]
    option_4b = data.get("choices")[i][1]
    option_4c = data.get("choices")[i][2]
    option_4d = data.get("choices")[i][3]
    i+=1 #q5
    question_prompt5 = data.get("question")[i]
    option_5a = data.get("choices")[i][0]
    option_5b = data.get("choices")[i][1]
    option_5c = data.get("choices")[i][2]
    option_5d = data.get("choices")[i][3]
    i+=1 #q6
    question_prompt6 = data.get("question")[i]
    option_6a = data.get("choices")[i][0]
    option_6b = data.get("choices")[i][1]
    option_6c = data.get("choices")[i][2]
    option_6d = data.get("choices")[i][3]
    i+=1 #q7
    question_prompt7 = data.get("question")[i]
    option_7a = data.get("choices")[i][0]
    option_7b = data.get("choices")[i][1]
    option_7c = data.get("choices")[i][2]
    option_7d = data.get("choices")[i][3]
    i+=1 #q8
    question_prompt8 = data.get("question")[i]
    option_8a = data.get("choices")[i][0]
    option_8b = data.get("choices")[i][1]
    option_8c = data.get("choices")[i][2]
    option_8d = data.get("choices")[i][3]
    i+=1 #q9
    question_prompt9 = data.get("question")[i]
    option_9a = data.get("choices")[i][0]
    option_9b = data.get("choices")[i][1]
    option_9c = data.get("choices")[i][2]
    option_9d = data.get("choices")[i][3]
    i+=1 #q10
    question_prompt10 = data.get("question")[i]
    option_10a = data.get("choices")[i][0]
    option_10b = data.get("choices")[i][1]
    option_10c = data.get("choices")[i][2]
    option_10d = data.get("choices")[i][3]

    return render_template(
        "quiz-2.html",
        question_prompt1="1. "+question_prompt1,
        option_1a=option_1a,
        option_1b=option_1b,
        option_1c=option_1c,
        option_1d=option_1d,
        question_prompt2="2. "+question_prompt2,
        option_2a=option_2a,
        option_2b=option_2b,
        option_2c=option_2c,
        option_2d=option_2d,
        question_prompt3="3. "+question_prompt3,
        option_3a=option_3a,
        option_3b=option_3b,
        option_3c=option_3c,
        option_3d=option_3d,
        question_prompt4="4. "+question_prompt4,
        option_4a=option_4a,
        option_4b=option_4b,
        option_4c=option_4c,
        option_4d=option_4d,
        question_prompt5="5. "+question_prompt5,
        option_5a=option_5a,
        option_5b=option_5b,
        option_5c=option_5c,
        option_5d=option_5d,
        question_prompt6="6. "+question_prompt6,
        option_6a=option_6a,
        option_6b=option_6b,
        option_6c=option_6c,
        option_6d=option_6d,
        question_prompt7="7. "+question_prompt7,
        option_7a=option_7a,
        option_7b=option_7b,
        option_7c=option_7c,
        option_7d=option_7d,
        question_prompt8="8. "+question_prompt8,
        option_8a=option_8a,
        option_8b=option_8b,
        option_8c=option_8c,
        option_8d=option_8d,
        question_prompt9="9. "+question_prompt9,
        option_9a=option_9a,
        option_9b=option_9b,
        option_9c=option_9c,
        option_9d=option_9d,
        question_prompt10="10. "+question_prompt10,
        option_10a=option_10a,
        option_10b=option_10b,
        option_10c=option_10c,
        option_10d=option_10d,


    )


# allows users to upload quiz
# @app.route("/create-quiz")
# def create_quiz():
#     csv_parse.csv_reader("quiz1")
#     return


# def is_logged(f):
# 	@wraps(f)
# 	def wrap(*args, **kwargs):
# 		if 'logged_in' in session:
# 			return f(*args, **kwargs)
# 		else:
# 			flash('Unauthorized, Please login','danger')
# 			return redirect(url_for('login'))
# 	return wrap
##This is a function for checking login. This function is invokved at every point of something requiring login

# Barebones for API Calls
# refs
# https://pythonbasics.org/flask-http-methods/
# https://stackoverflow.com/questions/40963401/flask-dynamic-data-update-without-reload-page/40964086

# @app.route('/', methods = ["POST"])
# def quiz_page():
# 	if question == max:
# 		if request.method == "POST":
# 			return redirect(url_for('results_page')

# 	if request.method == "POST":
# 		std_ans[request.form['$question num']] = request.form['$choice'].value
# 		return redirect(url_for('quiz_page',question=question+1))


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


if __name__ == "__main__":
    app.run(host="0.0.0.0")