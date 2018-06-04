from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tasks.models import Task
from application.tasks.lomakkeet import TehtäväLomake

@app.route("/tasks", methods=["GET"])
@login_required
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())

@app.route("/tasks/new/")
@login_required
def tasks_form():
    return render_template("tasks/new.html", lomake = TehtäväLomake())

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
    t.kayttaja_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))
