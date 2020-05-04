from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c1dd1056ef414905719940d2a9f3bef9'

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

if __name__ == '__main__':
    app.run(debug=True)