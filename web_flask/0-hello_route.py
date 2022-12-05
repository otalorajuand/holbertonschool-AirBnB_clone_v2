#!/usr/bin/python3
"""This module contains a simple app in flask"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"

app.run(host='0.0.0.0', port=5000)