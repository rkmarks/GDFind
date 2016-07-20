import os
from flask import Flask, render_template, redirect, url_for, request
from shared.forms import SearchForm
from geopy.geocoders import Nominatim

geolocator = Nominatim()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/', methods=['GET'])
def route_home():
    return redirect(url_for('route_search'))


@app.route('/search', methods=['GET', 'POST'])
def route_search():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Thanks for searching')
        return redirect(url_for('route_results'))
    return render_template('search.html', title='Search Here', form=form)


@app.route('/results', methods=['GET'])
def route_results():
    return render_template('results.html')


@app.route('/profile', methods=['GET'])
def route_profile():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0')
