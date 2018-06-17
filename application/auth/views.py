from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import Käyttäjä
from application.auth.lomakkeet import KirjautumisLomake, UusiLomake

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/kirjautuminen.html", lomake = KirjautumisLomake())

    lomake = KirjautumisLomake(request.form)

    user = Käyttäjä.query.filter_by(kayttajanimi=lomake.käyttäjänimi.data, salasana=lomake.salasana.data).first()
    if not user:
        return render_template("auth/kirjautuminen.html", lomake = lomake, error = "Käyttäjää ei ole olemassa, tai salasana on väärin")


    login_user(user)
    
    return redirect(url_for("index")) 

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  

@app.route("/auth/")
def auth_form():
    return  render_template("auth/new.html", lomake = UusiLomake())

@app.route("/auth/", methods = ["POST"])
def auth_create():
    lomake = UusiLomake(request.form)

    if not lomake.validate():
        print("täällä")
        return render_template("auth/new.html", lomake = lomake)
    if not lomake.salasana.data == lomake.salasana2.data:
        print("vai täällä")
        return render_template("auth/new.html", lomake = lomake)
        
    k = Käyttäjä(lomake.nimi.data)
    k.kayttajanimi = lomake.kayttajanimi.data
    k.salasana = lomake.salasana.data
    
    db.session().add(k)
    db.session().commit()

    return render_template("auth/kirjautuminen.html", lomake = KirjautumisLomake())
    


