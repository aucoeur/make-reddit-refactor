from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, ValidationError, URL

class EntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    url = URLField('Link', validators=[DataRequired(), URL()])
    submit = SubmitField('Create New Entry')
