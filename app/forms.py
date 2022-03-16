from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DriverForm(FlaskForm):
    drivername = StringField('Driver Name', validators=[DataRequired()])
    submit = SubmitField()