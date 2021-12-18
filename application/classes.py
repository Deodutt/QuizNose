from wtforms import Form, StringField, TextAreaField, PasswordField, validators, DateTimeField, BooleanField, IntegerField

class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=3, max=50)])
	username = StringField('Username', [validators.Length(min=4,max=25)])
	email = StringField('Email', [validators.Email()])
	password = PasswordField('Password', [
			validators.Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", message="Password should contain min 8 characters including 1 letter and 1 number."),
			validators.DataRequired(),
			validators.EqualTo('confirm', message="Password do not match")
		])
	confirm = PasswordField('Confirm Password')