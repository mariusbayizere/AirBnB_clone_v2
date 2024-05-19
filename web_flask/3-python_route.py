#!/usr/bin/python3
"""this module is responsible for printing message for Hello HBNB!"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """this module will print Hello HBNB message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """this module will print HBNB message"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """this module will print HBNB message"""

    replace_variable = text.replace('_', '')
    return 'C{}'.format(replace_variable)


@app.route('/python/', defaults={'text': ' is cool'})
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """this module will print HBNB message"""

    replace_variable = text.replace('_', '')
    return 'python{}'.format(replace_variable)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
