from flask import Flask
from download import download

app = Flask(__name__)


@app.route("/")
def hello_world():
    download()
    return "<p>Hello, World!</p>"
