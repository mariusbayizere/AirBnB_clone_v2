#!/usr/bin/python3
"""
using Flask to display our HBNB data, you will
need to update some part of our engine
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """function that will teardown"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def displayAllData():
    """function that will display all data on data"""
    state1 = storage.all(State)
    return render_template("8-cities_by_states.html",
                           Table="States", state1=state1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
