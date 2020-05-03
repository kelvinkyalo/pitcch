from flask import Flask, render_template
app = Flask(__name__)

pitches = [
    {
        'author' : 'Joan',
        'category' : 'Promotion'
        'content' : 'First pitch'
        'date_posted' : 'Apri; 20, 2020'
    },
    {
        'author' : 'Simon',
        'category' : 'Interview'
        'content' : 'Second pitch'
        'date_posted' : 'Apri; 10, 2020'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pitches=pitches)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)