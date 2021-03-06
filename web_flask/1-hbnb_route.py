#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
strict_slashes = False


@app.route("/", strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnb():
    return 'HBNB'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
