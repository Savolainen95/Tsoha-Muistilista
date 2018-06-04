from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.auth.models import Käyttäjä
from application.auth.lomakkeet import KirjautumisLomake

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