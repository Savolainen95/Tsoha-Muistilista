from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.luokka.models import Luokka
from application.luokka.lomakkeet import LuokkaLomake

@login_required

@app.route("/luokka", methods=["GET"])
@login_required
def luokka_index():
    return render_template("luokka/list.html", luokat = Luokka.query.all())

@app.route("/luokka/new/")
@login_required
def luokka_form():
    return render_template("luokka/new.html", lomake = LuokkaLomake())

@app.route("/luokka/", methods=["POST"])
@login_required
def luokka_create():

    lomake = LuokkaLomake(request.form)
    if not lomake.validate():
        return render_template("luokka/new.html", lomake = lomake)
    
    l = Luokka()
    l.nimi = lomake.nimi.data

    db.session.add(l)
    db.session.commit()
    
    return redirect(url_for("luokka_index"))

@app.route("/luokka/poista/<luokka_id>", methods=["POST"])
@login_required
def luokka_remove(luokka_id):
    l = Luokka.query.get(luokka_id)
    db.session.delete(l)
    db.session.commit()
    return redirect(url_for("luokka_index"))