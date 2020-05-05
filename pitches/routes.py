from flask import render_template, url_for, flash, redirect
from pitches import app, db, bcrypt
from pitches.forms import SignupForm, LoginForm
from pitches.models import User, Pitch

pitches = [
    {
        'author' : 'Joan',
        'category' : 'Promotion',
        'content' : 'First pitch',
        'date_posted' : 'April 30, 2020'
    },
    {
        'author' : 'Simon',
        'category' : 'Interview',
        'content' : 'Second pitch',
        'date_posted' : 'May 3, 2020'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pitches=pitches)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About Page')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been successfully created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        flash('Login Unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
