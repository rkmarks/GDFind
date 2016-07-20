from wtforms import Form, SelectField, StringField, validators


class SearchForm(Form):
    keyword = StringField('Keyword Search', [validators.required()])
    radius = SelectField('Miles Within',
                         choices=[
                                    ('5', 'Five'),
                                    ('10', 'Ten'),
                                    ('25', 'TwentyFive'),
                                    ('50', 'Fifty'),
                                    ('100', 'OneHunid')
                                 ])
