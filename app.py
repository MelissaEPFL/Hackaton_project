from get_context import get_time_spent

from flask import Flask

from datetime import datetime


app = Flask(__name__)

@app.route('/')

def hello():
    return get_time_spent("aw-watcher-window", "aw-watcher-window_LAPTOP-H8NECJ78", "devenv.exe")

