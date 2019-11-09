import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/obsgraph")
def obsgraph():
    """Return the OBS Graph page."""
    return render_template("obsgraph.html")

@app.route("/stacked")
def stacked():
    """Return the Stacked Graph page."""
    return render_template("stacked.html")


@app.route("/fun")
def fun():
    """Return the code page."""
    return render_template("fun.html")

if __name__ == "__main__":
    app.run()
