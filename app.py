from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c1dd1056ef414905719940d2a9f3bef9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,
                    primary_key=True)
    username = db.Column(db.String(20),
                        unique = True,
                        nullable =  False)
    email = db.Column(db.String(120),
                        unique = True,
                        nullable =  False)
    image_file = db.Column(db.String(20),
                            nullable = False,
                            default = 'default.jpg')
    password = db.Column(db.String(60),
                        nullable=False)

    # def __repr__(self):

                            

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'wamuyu@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)