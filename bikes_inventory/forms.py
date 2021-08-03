#import modules to create form and validate user input

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

#create userloginform and inherit flaskform attributes
class UserLoginForm(FlaskForm):
    #attritube email uses StringField class with label 'email' and validators
    email = StringField('Email', validators=[DataRequired(), Email()])
    #attribute password uses Passwordfield class with label and validators
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    #submit button takes submitfield class
    submit_button = SubmitField()