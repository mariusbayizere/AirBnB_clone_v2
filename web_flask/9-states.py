#!/usr/bin/python3
"""using Flask to display our HBNB data, you will
need to update some part of our engine"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """function that will teardown"""
    storage.close()


@app.route("/states/", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def displayAllData(id=None):
    """function that will display all data on data"""
    states = storage.all(State)

    if not id:
        stock_city = {value.id: value.name for value in states.values()}
        return render_template("7-states_list.html",
                               Table="States", items=stock_city)

    k = "State.{}".format(id)
    if k in states:
        return render_template(
            "9-states.html", Table="State: {}".format(states[k].name),
            items=states[k]
        )

    return render_template("9-states.html", items=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
