from flask_wtf import FlaskForm

class SignupForm(FlaskForm):
    username = StringField('Username')