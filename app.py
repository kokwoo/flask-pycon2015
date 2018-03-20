#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)
guesses = ['Python', 'Java', 'C++']


@app.route('/')
def index():
    return '<h1>Guess the Language!</h1>'


# Dynamic port / Dynamic URL

# Everytime we recieve an input from users the input have to be validated 
@app.route('/guess/<int:id>')
def guess(id):
    return ('<h1>Guess the Language!</h1>'
            '<p>My guess: {}</p>').format(guesses[id])


if __name__ == '__main__':
    app.run(debug=True)
