from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c1dd1056ef414905719940d2a9f3bef9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)