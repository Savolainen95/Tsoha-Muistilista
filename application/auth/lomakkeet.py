from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class KirjautumisLomake(FlaskForm):
    käyttäjänimi = StringField("Käyttäjänmi")
    salasana = PasswordField("Salasana")

    class Meta:
        csrf = False

class UusiLomake(FlaskForm):
    nimi = StringField("Nimi")
    kayttajanimi = StringField("Käyttäjänimi")
    salasana = StringField("Salasana")
    salasana2 = StringField("Salasana uudelleen")

    class Meta:
        csrf = False