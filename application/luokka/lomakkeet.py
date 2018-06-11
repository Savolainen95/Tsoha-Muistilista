from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField, IntegerField

class LuokkaLomake(FlaskForm):
    nimi = StringField("Luokan nimi",
    [validators.Length(min=2, max=30,
    message = "Luokan nimen pitää olla välillä 2-30." )])

    class Meta:
        csrf = False