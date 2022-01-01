from flask import Flask, request, render_template, flash, redirect, url_for, render_template_string
from flask_mail import Mail, Message
from flask_mysqldb import MySQL
from classes import RegisterForm
import db
from upload_test import upload_test_blueprint
from passlib.hash import sha256_crypt
from itsdangerous import URLSafeTimedSerializer
from functools import wraps
from emailverifier import Client
from threading import Thread
from random import randint
import socket
from functools import wraps
import secretstuff



app = Flask(__name__, template_folder="templates", static_url_path="/static")
app.register_blueprint(upload_test_blueprint)

app.config.update(
    DEBUG=True,
    SECRET_KEY= 'testkey', #needed for cookie sessions. add to secrets file later
    MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = secretstuff.emailusername,
	MAIL_PASSWORD = secretstuff.emailpassword

)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
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
print(f"Original List: {db.list_tables(db_table = 'final')}\n")

## This creates a table named <var>
# db.create_table(new_name="testing_purpose")
# print(f"New List: {db.list_tables(db_table = 'final')}\n")

## This deletes a table named <var>
# db.delete_table(target="testing_purpose")
# print(f"New List: {db.list_tables(db_table = 'final')}\n")


##here is email function for verification of account

# def get_local_ip():	
# 	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 	s.connect(('8.8.8.8', 1))
# 	local_ip_address = s.getsockname()[0]
# 	return local_ip_address

'''This here will grab the address of the host where it is hosting to create to be used in a url later on. IPBased commented out for now'''

mail = Mail(app)

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
htmlbody='''
Your account on <b>The Best</b> Quiz App was successfully created.
Please click the link below to confirm your email address and
activate your account:
  
<a href="{{ confirm_url }}">{{ confirm_url }}</a>
 <p>
--
Questions? Comments? Email </p>
'''


client = Client('at_rFxZz7zEX8CO8V5IDBfzexOe2fW8b')

def send_email(recipients,html_body):
	try:
		msg = Message(
            'Confirm Your Email Address',
		  sender="nycazn724@gmail.com",
		  recipients=recipients
          )
		msg.html = html_body
		send_async_email(app, msg)
		# return 'Mail sent!'
		return
	except Exception as e:
		# return(str(e))
		return



def send_confirmation_email(user_email):
	confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    ##https://stackoverflow.com/questions/34902378/where-do-i-get-a-secret-key-for-flask
 
	confirm_url = url_for('confirm_email',
		token=confirm_serializer.dumps(user_email, salt='email-confirmation-salt'),
		_external=True)
	local_ip = "127.0.0.1" #"get_local_ip() changed for testing
	x=""
	if 'localhost' in confirm_url:
		x=confirm_url.split("localhost:5000")
	else:
		x=confirm_url.split("127.0.0.1:5000")
	confirm_url = x[0] + local_ip + ":5000"+ x[1]
	html = render_template_string(htmlbody, confirm_url=confirm_url)

	send_email([user_email], html)
'''This here salts the secret key and creates a token based off the user email added to secret key'''


@app.route('/confirm/<token>')
def confirm_email(token):
	try:
		confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
		email = confirm_serializer.loads(token, salt='email-confirmation-salt', max_age=3600)
	except:
		flash('The confirmation link is invalid or has expired.', 'error')
		return redirect(url_for('login'))

	cur = db.db.cursor()
	results = cur.execute('SELECT * from users where email = %s' , [email])
	if results > 0:
		data = cur.fetchone()
		email_confirmed = data[5]
		if email_confirmed:
			flash('Account already confirmed. Please login.', 'info')
		else:
			results = cur.execute('UPDATE users SET confirmed = 1 where email = %s' , [email])
			db.db.commit()
			cur.close()
			flash('Thank you for confirming your email address!', 'success')
			return redirect(url_for('login'))
		return redirect(url_for('index'))

##end email

if __name__ == "__main__":
    app.run(host="0.0.0.0")