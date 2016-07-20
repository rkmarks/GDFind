from flask import Flask, render_template
from shared.forms import SearchForm
from geopy.geocoders import Nominatim

geolocator = Nominatim()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def route_home(keyword, zip, radius):
    redirect(url_for('route_search'))


@app.route('/search', methods=['GET', 'POST'])
def route_search():
    form = SearchForm()
    if request.method == 'POST' and form.validate():
        flash('Thanks for searching')
        redirect(url_for('route_results'))
    return render_template('results.html', form=form)


@app.route('/results', methods=['GET'])
def route_results():
    return


@app.route('/profile', methods=['GET'])
def route_profile():
    return
