from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	name= StringField('Name', 
		validators=[DataRequired(), Length(min=2,
		 max=20)])
	email = StringField('Email', 
		validators=[DataRequired(),Email()])
	password = PasswordField('Password', 
		validators=[DataRequired()])
	confirm_pasword = PasswordField('Confirm Password',
		validators = [DataRequired(), EqualTo('password')]
		)
	submit = SubmitField('Register')

class LoginForm(FlaskForm):
	email = StringField('Email', 
		validators=[DataRequired(),Email()])
	password = PasswordField('Password', 
		validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Register')


