from flask import Flask, request, jsonify, render_template
import db

# from functools import wraps

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

app = Flask(__name__, template_folder="templates", static_url_path="/static")

# def is_logged(f):
# 	@wraps(f)
# 	def wrap(*args, **kwargs):
# 		if 'logged_in' in session:
# 			return f(*args, **kwargs)
# 		else:
# 			flash('Unauthorized, Please login','danger')
# 			return redirect(url_for('login'))
# 	return wrap


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/studDash.html")
def studDash():
    return render_template("studDash.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


# This list all the tables inside the database final
print(f"Original List: {db.list_tables(db_table = 'final')}\n")

# This creates a table named <var>
db.create_table(new_name="testing_purpose")
print(f"New List: {db.list_tables(db_table = 'final')}\n")

# This deletes a table named <var>
db.delete_table(target="testing_purpose")
print(f"New List: {db.list_tables(db_table = 'final')}\n")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")