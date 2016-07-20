from flask_wtf import Form
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired


class SearchForm(Form):
    keyword = StringField('keyword',  validators=[DataRequired()])
    zipcode = StringField('zipcode')
    radius = SelectField('radius',
                         choices=[
                                    ('Five', '5'),
                                    ('Ten', '10'),
                                    ('TwentyFive', '25'),
                                    ('Fifty', '50'),
                                    ('Hunid', '100')
                                 ])
