#!/usr/bin/python3
"""
Python Script that starts a flask web application
"""
from flask import Flask
app = Flask(__name__)
strict_slashes = False


@app.route("/", strict_slashes=False)
def index():
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
