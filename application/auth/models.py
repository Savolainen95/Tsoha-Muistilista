from application import db
from sqlalchemy.sql import text



class Käyttäjä(db.Model):
    __tablename__ = "kayttaja"

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    kayttajanimi = db.Column(db.String(144), unique=True, nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

    tasks = db.relationship("Task", backref='task', lazy=True)

    
    
    def __init__(self, nimi):
        self.nimi = nimi
    

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def roles(self):
        return ["ADMIN"]


