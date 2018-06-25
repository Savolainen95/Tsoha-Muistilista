from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class KirjautumisLomake(FlaskForm):
    käyttäjänimi = StringField("Käyttäjänmi", [
        validators.DataRequired(message = "Nimeä ei syötetty")
        ])
    salasana = PasswordField("Salasana", [
        validators.DataRequired(message = "Salasanaa ei syötetty")
        ])

    class Meta:
        csrf = False

class UusiLomake(FlaskForm):
    nimi = StringField("Nimi", [
        validators.DataRequired(message = 'Kirjoita nimi')
    ])
    kayttajanimi = StringField("Käyttäjänimi", [
        validators.DataRequired(message = 'Kirjoita nimi')
    ])
    salasana = StringField("Salasana", [
        validators.DataRequired(message = 'Kirjoita salasana.'),
        
    ])
    salasana2 = StringField("Salasana uudelleen")

    class Meta:
        csrf = False