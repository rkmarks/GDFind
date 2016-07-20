from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def route_home(keyword, zip, radius):
    return


@app.route('/search', methods=['POST'])
def route_search():
    return


@app.route('/results', methods=['GET'])
def route_results():
    return


@app.route('/profile', methods=['GET'])
def route_profile():
    return
