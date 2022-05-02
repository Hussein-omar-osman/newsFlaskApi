from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import Length, DataRequired

class SearchForm(FlaskForm):
    SearchTerm = StringField('SearchTerm', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('search')