import os
import sys
import urllib2
import json
from flask import Flask, render_template, redirect, url_for, request, flash
from shared.forms import SearchForm
from geopy.geocoders import Nominatim


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

geolocator = Nominatim()

def convert_miles_to_meters(miles):
    conversion = int(miles)
    conversion = conversion * 1609.33999997549
    return conversion

@app.route('/', methods=['GET','POST'])
def route_home():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('route_results'), code=307)
    return render_template('search.html', title='Search Here', form=form)


@app.route('/results', methods=['GET', 'POST'])
def route_results():
    keyword = request.form['keyword']
    zipcode = str(request.form['zipcode'])
    radius = request.form['radius']
    location = geolocator.geocode(zipcode)
    lat = str(location.latitude)
    lon = str(location.longitude)
    # Find lat / long
    data = '{"api_key" : "c9caffc16e51883cfec43b1febf65cb898926037", "fields" : [ "name", "description", "website_url", "open_hours", "categories", "locu_id", "location", "contact" ], "venue_queries" : [ { "categories" : "' + keyword + '", "locu": { "is_publishable": true }, "location" : { "geo" : { "$in_lat_lng_radius" : [' + str(location.latitude) + ', ' + str(location.longitude) +', ' + str(convert_miles_to_meters(radius)) + '] } } } ] }'
    url = 'https://api.locu.com/v2/venue/search'

    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    for x in f:
        data = x
    f.close()

    parsed_json = json.loads(data)

    return render_template('results.html', json=parsed_json)



@app.route('/profile', methods=['GET'])
def route_profile():
    return

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
