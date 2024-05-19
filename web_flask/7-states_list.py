#!/usr/bin/python3
"""
using Flask to display our HBNB data, you will
need to update some part of our engine
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """function that will teardown"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def displayAllData():
    """function that will display all data on data"""
    states = storage.all(State)
    datas = {value.id: value.name for value in states.values()}
    return render_template("7-states_list.html",
                           Table="States", items=datas)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
