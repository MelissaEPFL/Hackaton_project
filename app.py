from get_context import *

from flask import Flask

from datetime import datetime


app = Flask(__name__)

@app.route('/')

def hello():
    return get_last_time_on("vscode")

