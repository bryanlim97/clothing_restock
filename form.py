"""Form class to accept inputs."""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SignupForm(FlaskForm):
	"""Specifies correct fields and instructions corresponding to them."""

	product_name = StringField('Enter product name here:')
	size = StringField('Enter size here (ex. XS, S, M, L):')
	product_url = StringField('Enter product url here:')
	submit = SubmitField()
