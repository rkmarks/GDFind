import os
import sys
import urllib2
from flask import Flask, render_template, redirect, url_for, request, flash
from shared.forms import SearchForm
from geopy.geocoders import Nominatim


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

geolocator = Nominatim()



@app.route('/', methods=['GET'])
def route_home():
    return redirect(url_for('route_search'))


@app.route('/search', methods=['GET'])
def route_search():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Thanks for searching')
        return redirect(url_for('route_results', keyword=request.form['keyword'], zipcode=request.form['zipcode'], radius=request.form['radius']))
    return render_template('search.html', title='Search Here', form=form)


@app.route('/results', methods=['GET', 'POST'])
def route_results():
    # location = geolocator.geocode()
    """        data = '{"api_key" : "c9caffc16e51883cfec43b1febf65cb898926037", "fields" : [ "name", "description", "website_url", "open_hours", "categories", "locu_id", "location", "contact" ], "venue_queries" : [ { "categories" : "' + cat + '", "locu": { "is_publishable": true }, "location" : { "geo" : { "$in_lat_lng_radius" : [' + lat + ', ' + lon +', ' + rad + '] } } } ] }'
            url = 'https://api.locu.com/v2/venue/search'

            req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
            f = urllib2.urlopen(req)
            for x in f:
                print(x)
            f.close()
    """
    return render_template('results.html')


@app.route('/profile', methods=['GET'])
def route_profile():
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0')
