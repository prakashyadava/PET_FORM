from flask_wtf import FlaskForm
from wtforms import(StringField,SelectField,SubmitField,HiddenField)
class PetForm(FlaskForm):
    pet = StringField('Enter pet name? ')
    owner = StringField("Enter owner name: ")
    pet_breed = SelectField("Select Animal Breed ",choices=[('dog','Dog'),('cat','Cat')])
    submit = SubmitField('Submit')
class UpdateForm(FlaskForm):
    pet = StringField('Enter pet name? ')
    pet_id = HiddenField()
    owner = StringField("Enter owner name: ")
    pet_breed = SelectField("Select Animal Breed ",choices=[('dog','Dog'),('cat','Cat')])
    submit = SubmitField('Submit')
