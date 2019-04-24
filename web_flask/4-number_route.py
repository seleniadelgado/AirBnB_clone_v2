#!/usr/bin/python3
"""script that starts a flask application
"""
from flask import Flask
app = Flask(__name__)
app.strict_slashes = False


@app.route("/", strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnb():
    return 'HBNB'


@app.route("/c/<text>")
def c(text):
    text = text.replace('_', ' ')
    a = "C {}".format(text)
    return a


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = text.replace('_', ' ')
    a = "Python {}".format(text)
    return a


@app.route('/number/<int:n>')
def number(n, strict_slashes=False):
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
