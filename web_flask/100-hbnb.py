#!/usr/bin/python3
"""using Flask to display our HBNB data, you will
need to update some part of our engine"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """function that will teardown"""
    storage.close()


@app.route("/hbnb/", strict_slashes=False)
def display_AllData():
    """function that will display all data on data"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)

    return render_template(
        "100-hbnb.html",
        states=states.values(),
        amenities=amenities.values(),
        places=places.values(),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
