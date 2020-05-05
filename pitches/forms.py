from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from pitches.models import User

class SignupForm(FlaskForm):
    username = StringField('Username', 
                validators=[DataRequired(), 
                Length(min=2, max=20)])
    email = StringField('Email',
            validators=[DataRequired(),
            Email()])
    password = PasswordField('Password',
                validators=[DataRequired(),
                Length(min=8, max=16)])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(),
                        EqualTo('password'),
                        Length(min=8, max=16)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()            
            if user:
                    raise ValidationError('That username is taken. Please choose another one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
            validators=[DataRequired(),
            Email()])
    password = PasswordField('Password',
                validators=[DataRequired(),
                Length(8)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')