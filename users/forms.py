from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, Length, DataRequired, NoneOf, ValidationError
import re


def character_check():
    def _character_check(form, field):
        p = re.compile(r'[,\&<%]')
        if p.match(field.data):
            raise ValidationError("must not contain characters : <,&,%")
    return _character_check

class RegisterForm(FlaskForm):
    username = StringField(validators=[
        DataRequired(),
        Email(),
        character_check()])

    password = PasswordField(validators=[
        DataRequired(),
        Length(8,15,"Please use 8 to 15 characters"),
        character_check()])

    submit = SubmitField()

    def validate_password(form, field):
        p = re.compile(r'^(?=.*\d)(?=.*[a-z]).+$')
        if not p.match(field.data):
            raise ValidationError("Password must contain 1 digit and one lowercaseletter between a and z")

