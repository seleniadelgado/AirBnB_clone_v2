#!/usr/bin/python3
"""Updating part of engine"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLalchemy Session"""
    storage.close()


@app.route("/states_list")
def display_states():
    states_l = storage.all("State").values()
    return render_template('7-states_list.html', states_l=states_l)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
