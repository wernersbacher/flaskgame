from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from app.models.User import User

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		name = username.data
		if len(name) > 13:
			raise ValidationError('Maximum of 13 letters allowed.')
		if len(name) < 3:
			raise ValidationError('Minimum are 3 letters.')

		user = User.query.filter_by(username=name).first()
		if user is not None:
			raise ValidationError('This username is already taken.')

	def validate_password(self, password):
		pw = password.data
		if len(pw) < 4:
			raise ValidationError('Your password should be at least 4 characters long.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('This email address is already taken.')
