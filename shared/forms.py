from flask_wtf import Form
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired


class SearchForm(Form):
<<<<<<< HEAD
    keyword = StringField('keyword', validators=[DataRequired()])
    zipcode = StringField('zipcode')
=======
    keyword = StringField('keyword', id='mainSearch', render_kw = {"placeholder": "Keyword"}, validators=[DataRequired()])
    zipcode = StringField('zipcode', id="zipSearch", render_kw = {"placeholder": "Postal Code"})
>>>>>>> df62d88bd8defdbd864ae0021d8efd621ca77212
    radius = SelectField('radius',
                         choices=[
                                    ('5', '5'),
                                    ('10', '10'),
                                    ('25', '25'),
                                    ('50', '50'),
                                    ('100', '100')
                                 ])
