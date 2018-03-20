#!/usr/bin/env python
# ^ which interpreter i want to run 

from flask import Flask

# Everytime you can the flask application flask needs to know where the files
# are - by passing a python variable "__name__" flask will be able to find where
# the module is and locate the files accordingly
app = Flask(__name__)


# Main entry point of the application

# Return the html title via the return

# When you prepend a "@" to a function it is called a decorator what it does is
# to modify functions in different ways in this case it will create a mapping
# between the url and the function flask now knows when some one types the root
# url in the browser it will return the correct function

# Flask needs an obj to represent tha application in this case "app"
@app.route('/')
def index():
    return '<h1>Guess the Language!</h1>'

# This is how we start the main application, via a webserver. Flask comes with a
# webserver by simplfying the set up. 

# "debug true" enables debug functions

# if statement helps to seperate is from running this file as the main file as
# well as running this file from another file.
if __name__ == '__main__':
    app.run(debug=True)
