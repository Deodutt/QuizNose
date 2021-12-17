from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine
from functools import wraps


app = Flask(__name__, template_folder="templates")

# Connect to database
engine = create_engine(
    "mysql+pymysql://admin:KuraLabs#123@database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com:3306/final",
) ##change endpoint here reference from terraform config and variable

@app.route('/')
def index():
	return render_template('index.html')

def is_logged(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorized, Please login','danger')
			return redirect(url_for('login'))
	return wrap
##This is a function for checking login. This function is invokved at every point of something requiring login


def list_tables():
    list_of_tables = engine.table_names()
    return list_of_tables


print(list_tables())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
