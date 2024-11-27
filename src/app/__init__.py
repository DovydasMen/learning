from flask import Flask

app = Flask(__name__)

from app.routes import hello_world
from app.routes import wind