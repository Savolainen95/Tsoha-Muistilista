from application import db
from sqlalchemy.sql import text
from application.luokka.models import Luokka

apu = db.Table('taskluokka',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('luokka_id', db.Integer, db.ForeignKey('luokka.id'), primary_key=True)
)

class Task(db.Model):
    __tablename__='task'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    urgent = db.Column(db.Integer)
    time = db.Column(db.Integer, nullable=True)

    apu = db.relationship('Luokka', secondary=apu, lazy='subquery',
        backref=db.backref('Task', lazy=True))

    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'),
                           nullable=False)

    def __init__(self, name, apu):
        self.name = name
        self.done = False
        self.apu = apu


    @staticmethod
    def askareen_luokat(apuid):

        string = ()
        stmt = text('SELECT luokka.nimi FROM task, luokka, taskluokka'
        ' WHERE taskluokka.task_id = ' + str(apuid) +
        ' AND taskluokka.luokka_id = luokka.id'
        ' AND taskluokka.task_id = task.id')

        res = db.engine.execute(stmt)
        luokat = []
        for row in res:
            luokat.append(row[0])
        return luokat

   



        


        