from wtforms import Form, StringField, PasswordField, validators

class RegisterForm(Form):
	name = StringField('Name', [
		validators.Length(min=3, max=30),
		validators.Regexp(r"^\w+$", message = "Cannot include spaces")
		])
	username = StringField('Username', [
		validators.Length(min=4,max=30),
		validators.Regexp(r"^\w+$", message = "Cannot include spaces")
	])
	teachercode = StringField('Teachercode',[validators.optional(True)])
	email = StringField('Email', [
		validators.Email(),
		validators.Length(min=5, max=30)
		])
	password = PasswordField('Password', [
			validators.Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", message="Password should contain min 8 characters including 1 letter and 1 number."),
			validators.DataRequired(),
			validators.EqualTo('confirm', message="Password do not match"),
			validators.Length(min=8, max=30)
		])
	confirm = PasswordField('Confirm Password')

	##this class is necessary to create parameters for what the registration parameters are