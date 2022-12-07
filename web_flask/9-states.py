#!/usr/bin/python3
"""
starts a Flask web app
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """display a HTML with the states of the db"""
    states = storage.all(State)
    return render_template(
        '7-states_list.html',
        states=sorted(
            states.values(),
            key=lambda x: x.name))


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """display a HTML with the states of the db"""
    states = storage.all(State)
    flag = True if 'State.' + id in states else False
    state = states['State.' + id] if flag else None
    return render_template(
        '9-states.html',
        state=state,
        flag=flag)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
