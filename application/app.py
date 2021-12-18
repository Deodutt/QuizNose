from flask import Flask, request, jsonify, render_template
# from functools import wraps
from classes import RegisterForm


app = Flask(__name__, template_folder="templates", static_url_path='/static')

# metadata = MetaData()
# db = SQLAlchemy()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/register')
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data 
		email = form.email.data

		#email verifier	
		data = client.get(email)
		if str(data.smtp_check) == 'False':
			flash('Invalid email, please provide a valid email address','danger')
			return render_template('register.html', form=form)

		# send_confirmation_email(email) ##not neaded yet.

		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))
		cur = mysql.connection.cursor()
		cur.execute('INSERT INTO users(username,name,email, password,confirmed) values(%s,%s,%s,%s,0)', (username,name, email, password))
		mysql.connection.commit()
		cur.close()
		flash('Thanks for registering!  Please check your email to confirm your email address.', 'success')
		return redirect(url_for('login')) 
		# change in login function to redirect to warning page

	return render_template('register.html', form=form)

@app.route('/studDash.html')
def studDash():
	return render_template('studDash.html')

@app.route('/quiz')
def quiz():
	return render_template('quiz.html')



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


#Barebones for API Calls
#refs
#https://pythonbasics.org/flask-http-methods/
#https://stackoverflow.com/questions/40963401/flask-dynamic-data-update-without-reload-page/40964086

# @app.route('/', methods = ["POST"])
# def quiz_page():
# 	if question == max:
# 		if request.method == "POST":
# 			return redirect(url_for('results_page')

# 	if request.method == "POST":
# 		std_ans[request.form['$question num']] = request.form['$choice'].value 
# 		return redirect(url_for('quiz_page',question=question+1))


# Connect to database
# engine = create_engine(
#     "mysql+pymysql://admin:KuraLabs#123@database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com:3306/final",
# )


# def list_tables():
#     list_of_tables = engine.table_names()
#     return list_of_tables


# def create_table():
#     # checking the table list
#     list_of_tables = engine.table_names()
#     table_name = "user_info"

#     if table_name in list_of_tables:
#         print(f"The table '{table_name}' is inside the database!")

#     else:
#         user_info = Table(
#             table_name,
#             metadata,
#             Column("username", VARCHAR(20), primary_key=True),
#             Column("password", VARCHAR(20)),
#             Column("email", VARCHAR(20)),
#         )
#         metadata.create_all(engine)
#         print(f"The table '{table_name}' was successfully created!")
#     return


# def delete_table():
#     # checking the table list
#     list_of_tables = engine.table_names()
#     table_name = "users"

#     if table_name in list_of_tables:
#         print(f"The table '{table_name}'  was deleted from the database!")

#     else:
#         print(f"The table '{table_name}'  is not inside the database!")

#     return


# print(f"Original List: {list_tables()}\n")
# create_table()
# print(f"New List: {list_tables()}\n")
# # delete_table()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
