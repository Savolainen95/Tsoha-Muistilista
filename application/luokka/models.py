from application import db
from sqlalchemy.sql import text




class Luokka(db.Model):
    __tablename__ = "luokka"

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)

    @staticmethod
    def luokan_askareet():
        stmt = text('SELECT task.id FROM taskluokka'
        ' INNER JOIN task ON taskluokka.task_id = task.id '
        ' INNER JOIN luokka ON taskluokka.luokka_id = luokka.id'
        ' WHERE luokka.id = ' + id)
        res = db.engine.execute(stmt)

        return res