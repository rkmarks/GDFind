from wtforms import Form, SelectField, StringField, validators


class SearchForm(Form):
    keyword = StringField('Keyword Search', [validators.required()])
    zipcode = StringField('Zip Code')
    radius = SelectField('Miles Within',
                         choices=[
                                    ('Five', '5'),
                                    ('Ten', '10'),
                                    ('TwentyFive', '25'),
                                    ('Fifty', '50'),
                                    ('Hunid', '100')
                                 ])
