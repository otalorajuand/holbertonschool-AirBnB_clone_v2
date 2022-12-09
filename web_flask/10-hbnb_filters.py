#!/usr/bin/python3
"""
starts a Flask web app
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def state_cities():
    """display a HTML with the states of the db"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    print(states)
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
