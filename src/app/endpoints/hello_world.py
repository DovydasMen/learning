from app import app
from flask import request

@app.route("/")
def hello_world():
    return "<p> Hello World! <p>"