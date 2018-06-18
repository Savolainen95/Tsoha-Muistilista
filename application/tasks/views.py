from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tasks.models import Task
from application.tasks.lomakkeet import TehtäväLomake, MuokkausLomake
from application.auth.models import Käyttäjä
from application.luokka.models import Luokka
from application.luokka.lomakkeet import LuokkaLomake


@app.route("/tasks", methods=["GET"])
@login_required
def tasks_index():

    return render_template("tasks/list.html", tasks = Task.query.all(), id = current_user.id)

@app.route("/tasks/new/")
@login_required
def tasks_form():
    return render_template("tasks/new.html", lomake = TehtäväLomake(), luokat = Luokka.query.all(), lista = [])

@app.route("/tasks/specs/<task_id>/", methods=["POST"])
@login_required
def tasks_avaa_yksittainen(task_id):
    t = Task.query.get(task_id)
    return render_template("tasks/specs.html", askare = t)

@app.route("/tasks/modify/<task_id>/", methods=["POST"])
@login_required
def tasks_muokkaa(task_id):
    t = Task.query.get(task_id)
    return render_template("tasks/modify.html", askare = t, lomake = MuokkausLomake())

@app.route("/tasks/modify/do/<task_id>/", methods=["POST"])
@login_required
def tasks_muokkaa_hyvaksy(task_id):
    lomake = MuokkausLomake(request.form)
    t = Task.query.get(task_id)
    
    if not lomake.validate():
        return render_template("tasks/modify.html", askare = t, lomake = MuokkausLomake())
        
    

    t.name = lomake.nimi.data
    t.done = lomake.tehty.data
    
    t.urgent = lomake.kiireellisyys.data
    t.time = lomake.aikavaatimus.data

    db.session().commit()

    return render_template("tasks/specs.html/", askare = t)




@app.route("/tasks/poista/<task_id>", methods=["POST"])
@login_required
def tasks_remove(task_id):
    t = Task.query.get(task_id)
    db.session.delete(t)
    db.session.commit()
    return redirect(url_for("tasks_index"))

@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    if t.done == True:
        t.done = False
    else:
        t.done = True
    db.session().commit()
  
    return redirect(url_for("tasks_index"))



@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    

    lomake = TehtäväLomake(request.form)
    if not lomake.validate():
        return render_template("tasks/new.html", lomake = lomake)
        
    t = Task(lomake.nimi.data)
    t.done = lomake.tehty.data
    
    t.urgent = lomake.kiireellisyys.data
    t.time = lomake.aikavaatimus.data

    t.kayttaja_id = current_user.id


    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

