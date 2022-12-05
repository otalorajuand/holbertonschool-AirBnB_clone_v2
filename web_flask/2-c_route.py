#!/usr/bin/python3
"""
This module contains a simple app in flask
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """defines the return for the index"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """defines the return the /hbnb url"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f'C {text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
