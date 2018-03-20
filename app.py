#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
questions = ['Is it compiled?', 'Does it run on a VM?']
guesses = ['Python', 'Java', 'C++']

# Include 0 logic in the templates
# Web forms - To accept input from users by adding a form to the application 

@app.route('/')
def index():
    return render_template('index.html')

# When building the route by default it will sent a GET request
@app.route('/question/<int:id>', methods=['GET', 'POST'])
def question(id):
    if request.method == 'POST':
        if request.form['answer'] == 'yes':
            # redirect or render a new page
            # if the answer is yes, go to the next question
            
            # url for can be used in both in a python script or templates this
            # ensure the all urls are in one place
            
            # If request.forms remains loaded with the data after a redirect,
            # that only exists in the context of the request. It does not carry
            # the data with it after redirect is carry out.
            return redirect(url_for('question', id=id+1))
    return render_template('question.html', question=questions[id])


@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=guesses[id])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
