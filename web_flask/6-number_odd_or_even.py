#!/usr/bin/python3
"""this module is responsible for printing message for Hello HBNB!"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """this module will print HBNB message"""

    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    """this module will print HBNB message"""

    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """This module will print HBNB message"""

    message = ' even' if n % 2 == 0 else ' odd'
    datas = {
            "number": n,
            "message": message
            }

    return render_template('6-number_odd_or_even.html', datas=datas)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
