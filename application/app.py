from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from flask_mysqldb import MySQL
from classes import RegisterForm
import db
import csv_parse
from wtforms import Form, StringField,TextAreaField,PasswordField, validators, DateTimeLocalField, BooleanField, IntegerField, ValidationError
from passlib.hash import sha256_crypt
# from functools import wraps

app = Flask(__name__, template_folder="templates", static_url_path="/static")
# mysql = MySQL(app) //question. if db already invokes the sql library. do we need to reinvoke here?
app.secret_key= 'testkey'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")



@app.route('/register', methods=['GET','POST'])
def register():
    print(dir(db.db))
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        email = form.email.data

#         # email verifier
#         # data = client.get(email) ##commented out for now
#         # if str(data.smtp_check) == 'False': ##commented out for now
#         # flash('Invalid email, please provide a valid email address','danger')
#         # return render_template('register.html', form=form)

#         # send_confirmation_email(email) ##not neaded yet.

        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        cur = db.db.cursor()
        cur.execute(
            "INSERT INTO users(username,name,email, password,confirmed) values(%s,%s,%s,%s,0)",
            (username, name, email, password),
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


@app.route("/quiz")
def quiz():
    data = db.grab_question("q1")
    question_prompt = data.get("choices")[0]
    option_a = data.get("choices")[0]
    option_b = data.get("choices")[1]
    option_c = data.get("choices")[2]
    option_d = data.get("choices")[3]

    return render_template(
        "quiz.html",
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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")