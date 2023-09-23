#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
* /hbnb: Display the HTML page for hbnb home page.
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays the HTML page for hbnb home page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states,
                           places=places,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(excpt=None):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
