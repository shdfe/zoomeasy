from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import validators
from datetime import datetime
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateTimeLocalField

class ClassForm(FlaskForm):
    class_name = StringField('Class Name', validators=[DataRequired()])
    class_link = StringField('Zoom Link', validators=[DataRequired(), validators.regexp(r'https://(.*\.)?zoom.us/[a-z]/.+?\b')]) 
    start_time = DateTimeLocalField('Start Date and Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    end_time = DateTimeLocalField('End Date and Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Submit')

    