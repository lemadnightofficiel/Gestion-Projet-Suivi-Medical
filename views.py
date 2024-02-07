from flask import Blueprint, render_template, request, flash, redirect, url_for
import database_functions

views = Blueprint(__name__, "views")

@views.route("/", methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pasword = request.form.get('password')
        if database_functions.check_user(username):
            return redirect(url_for("views.form", username=username))
    return render_template("login.html")

@views.route("/form/<username>", methods = ['GET','POST'])
def form(username):
    if database_functions.check_date(username):
        return redirect(url_for("views.report")) #renvoie l'utilisateur vers la page suivante
    
    if request.method == 'POST':
        height = int(request.form.get('height'))
        weight = int(request.form.get('weight'))
        bpm = int(request.form.get('bpm'))
        oxy_sat = int(request.form.get('oxy_sat'))
        tas = int(request.form.get('tas'))
        tad = int(request.form.get('tad'))
        #check info
        if tas < tad :
            return
        #if correct add to database
        medical_values = (height, weight, bpm, oxy_sat, tas, tad)
        database_functions.send_to_medicalinfo_db(medical_values,username)
        return redirect(url_for("views.report")) #renvoie l'utilisateur vers la page suivante

    return render_template("form.html")

@views.route("/report")
def report():
    
    return render_template("index.html")


