from flask_wtf import Form
from wtforms import StringField, RadioField


choices = [("Yes", 'Yes'), ("No", 'No')]



class SurveyForm(Form):
    full_name = StringField(u'Full Name')
    choice = RadioField(u'Select One Choice',choices=choices)
