from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def route_home(keyword, zip, radius):
    return


@app.route('/results')
def route_results():
    return


@app.route('/profile')
def route_profile():
    return
