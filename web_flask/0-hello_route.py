#!/usr/bin/python3
"""this module is responsible for printing message for Hello HBNB!"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """this module will print Hello HBNB message"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
