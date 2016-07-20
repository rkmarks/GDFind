from flask_wtf import Form
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired


class SearchForm(Form):
    keyword = StringField('keyword', validators=[DataRequired()])
    zipcode = StringField('zipcode')
    radius = SelectField('radius',
                         choices=[
                                    ('5', '5'),
                                    ('10', '10'),
                                    ('25', '25'),
                                    ('50', '50'),
                                    ('100', '100')
                                 ])
