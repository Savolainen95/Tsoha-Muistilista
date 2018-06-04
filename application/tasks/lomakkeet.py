from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class TehtäväLomake(FlaskForm):
    nimi = StringField("Askareen nimi",
    [validators.Length(min=2, max=7,
     message = "Askareen pituuden pitää olla välillä 2-7." )])
    tehty = BooleanField("Onko askare tehty?")

    class Meta:
        csrf = False