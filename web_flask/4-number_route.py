#!/usr/bin/python3
"""
starts a Flask web app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """display “C ” followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """display “Python ” followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    """display “n is a number” only if n is an integer"""
    if int(n):
        return "n is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
