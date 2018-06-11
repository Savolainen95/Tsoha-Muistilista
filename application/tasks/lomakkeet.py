from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField, IntegerField

class TehtäväLomake(FlaskForm):
    nimi = StringField("Askareen nimi",
    [validators.Length(min=2, max=30,
    message = "Askareen pituuden pitää olla välillä 2-30." )])
    tehty = BooleanField("Onko askare tehty?")
    kiireellisyys = IntegerField("Kiirellinen")
    aikavaatimus = IntegerField("Aikavaatimus tunteina")

    class Meta:
        csrf = False

class MuokkausLomake(FlaskForm):
    nimi = StringField("Uusi nimi",
    [validators.Length(min=2, max=30,
    message = "Askareen pituuden pitää olla välillä 2-30.")])
    kiireellisyys = SelectField("Kiireellisyys", 
    choices = [(1, 'Ei'), (2, 'Kyllä')])
    