#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)
guesses = ['Python', 'Java', 'C++']

# Replacing the hardcoded string with a native flask function called
# render_template, passing in the html page

# Templates helps to seprate logic from presentation 
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=guesses[id])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
