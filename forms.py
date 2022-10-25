from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, URL

class AddCupcakeForm(FlaskForm):
    """ Form for adding cupcakes """

    flavor = StringField('Flavor', validators=[InputRequired()])
    size = StringField('Size', validators=[InputRequired()])
    rating = IntegerField('Rating', validators=[InputRequired()])
    image = StringField('Image URL', validators=[InputRequired()])