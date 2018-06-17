from application import db
from sqlalchemy.sql import text




class Luokka(db.Model):
    __tablename__ = "luokka"

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)

    @staticmethod
    def luokan_askareet(apuid):
        stmt = text('SELECT task.name FROM taskluokka, task, luokka'
        ' WHERE taskluokka.luokka_id = ' + str(apuid) +
        ' AND taskluokka.luokka_id = luokka.id'
        ' AND taskluokka.task_id = task.id')

        res = db.engine.execute(stmt)
        askareet = []
        for row in res:
            askareet.append(row[0])
        return askareet