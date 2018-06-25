from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SelectField, IntegerField, SelectMultipleField, widgets
from application.luokka.models import Luokka

class TehtäväLomake(FlaskForm):
    nimi = StringField("Askareen nimi",
    [validators.Length(min=2, max=30,
    message = "Askareen pituuden pitää olla välillä 2-30.")])
    tehty = BooleanField("Onko askare tehty?")
    kiireellisyys = IntegerField("Kiirellinen")
    aikavaatimus = IntegerField("Aikavaatimus tunteina")

    apu = SelectMultipleField("Luokat", coerce=int, validators = [],
        widget=widgets.ListWidget(prefix_label=True),
        option_widget=widgets.CheckboxInput())
    
    
        
    class Meta:
        csrf = False
    


class MuokkausLomake(FlaskForm):
    nimi = StringField("Uusi nimi",
    [validators.Length(min=2, max=30,
    message = "Askareen pituuden pitää olla välillä 2-30.")])
    kiireellisyys = IntegerField("Kiireellinen")
    aikavaatimus = IntegerField("Aikavaatimus tunteina", [

        validators.NumberRange(min=0, max=100, message= "Aikavaatimuksen voi olla vain 0 - 100 tuntia.")
    ])
    tehty = BooleanField("Onko askare tehty?")

    class Meta:
        csrf = False
    