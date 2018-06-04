from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

class KirjautumisLomake(FlaskForm):
    käyttäjänimi = StringField("Käyttäjänmi")
    salasana = PasswordField("Salasana")

    class Meta:
        csrf = False