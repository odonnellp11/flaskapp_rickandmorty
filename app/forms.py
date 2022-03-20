from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    charactername = StringField('Character Name', validators=[DataRequired()])
    submit = SubmitField()