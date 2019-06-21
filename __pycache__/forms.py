from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from academia_web.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = StringField('Password',validators=[DataRequired()])
	confirm_password = StringField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign Up')


	def validate_username(self,username):
		user= User.query.filter_by(username=username.data).first()
		if user :
			raise ValidationError('That username exists!!,please enter another')


	def validate_email(self,email):
		user= User.query.filter_by(email=email.data).first()
		if user :
			raise ValidationError('That email exists!!,please enter another')

class LoginForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	password = StringField('Password',validators=[DataRequired(),Length(max=9)])
	remember = BooleanField('Remember Me')
	submit=SubmitField('Login')

	

class UpdateAccountForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',validators=[DataRequired(),Email()])
	submit=SubmitField('Update')

	def validate_username(self,username):
		if username.data!=current_user.username:
			user= User.query.filter_by(username=username.data).first()
			if user :
				raise ValidationError('That username exists!!,please enter another')


	def validate_email(self,email):
		if email.data!=current_user.email:
			user= User.query.filter_by(email=email.data).first()
			if user :
				raise ValidationError('That email exists!!,please enter another')
