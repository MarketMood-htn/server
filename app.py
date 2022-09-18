from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/search")
def search():
    return "Welcome to the seach page"

@app.route("/explore")
def explore():
    return "Welcome to the explore page"