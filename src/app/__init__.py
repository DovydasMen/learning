from flask import Flask

app = Flask(__name__)

from app.endpoints import hello_world
from app.endpoints import wind
from app.endpoints import calc