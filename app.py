import os
import sys
import urllib2
from flask import Flask, render_template, redirect, url_for, request, flash
from shared.forms import SearchForm
from geopy.geocoders import Nominatim


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

geolocator = Nominatim()


@app.route('/', methods=['GET','POST'])
def route_home():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('route_results'), code=307)
    return render_template('search.html', title='Search Here', form=form)


@app.route('/results', methods=['GET', 'POST'])
def route_results():
    keyword = request.form['keyword']
    zipcode = request.form['zipcode']
    radius = request.form['radius']
    return render_template('results.html', radius=radius, keyword=keyword, zipcode=zipcode)


@app.route('/profile', methods=['GET'])
def route_profile():
    return

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
