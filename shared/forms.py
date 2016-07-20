from flask_wtf import Form
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired


class SearchForm(Form):
    keyword = StringField('keyword', id='mainSearch', validators=[DataRequired()])
    zipcode = StringField('zipcode', id="zipSearch", description="Current User Zip")
    radius = SelectField('radius',
                         choices=[
                                    ('5', '5'),
                                    ('10', '10'),
                                    ('25', '25'),
                                    ('50', '50'),
                                    ('100', '100')
                                 ])
