from wtforms import Form, SelectField, StringField, validators


class RegistrationForm(Form):
    keyword = StringField('Keyword Search',
                          [
                            validators.Length(min=1, max=36)
                            validators.DataRequired()
                          ])
    radius = SelectField('Miles Within',
                         choices=[
                                                 ],
                                    [validators.Length(min=6, max=35)])
