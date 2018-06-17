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
    
    @staticmethod
    def käyttäjät_ilman_askaretta():
        stmt = text("SELECT kayttaja.id, kayttaja.nimi FROM kayttaja"
                    " LEFT JOIN task ON task.kayttaja_id = kayttaja.id"
                    " WHERE (task.done IS null OR task.done == 1)"
                    " GROUP BY kayttaja.id"
                    " HAVING COUNT(task.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "nimi":row[1]})

        return response


