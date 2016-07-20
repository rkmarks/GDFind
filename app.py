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
    location = geolocator.geocode("85254")
    # Find lat / long
    data = '{"api_key" : "c9caffc16e51883cfec43b1febf65cb898926037", "fields" : [ "name", "description", "website_url", "open_hours", "categories", "locu_id", "location", "contact" ], "venue_queries" : [ { "categories" : "' + keyword + '", "locu": { "is_publishable": true }, "location" : { "geo" : { "$in_lat_lng_radius" : [' + location.latitude + ', ' + location.longitude +', ' + radius + '] } } } ] }'
    url = 'https://api.locu.com/v2/venue/search'

    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    req = urllib.request.Request(url, data, headers)
    for x in f:
        json = x
    f.close()

    return render_template('results.html', json=json)


@app.route('/profile', methods=['GET'])
def route_profile():
    return

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
