#!/usr/bin/python3
"""
starts a Flask web app
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """display a HTML with the states of the db"""
    states = storage.all(State)
    return render_template(
        '8-cities_by_states.html',
        states=sorted(
            states.values(),
            key=lambda x: x.name))


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
