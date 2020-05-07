from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    category = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class ReviewsForm(FlaskForm):
    review= TextAreaField('Write a review...', validators=[DataRequired()])
    submit = SubmitField('Submit')
