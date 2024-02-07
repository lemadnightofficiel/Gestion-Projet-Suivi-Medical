from flask import Blueprint, render_template, request, flash, redirect, url_for
import database_functions

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/form/<username>", methods = ['GET','POST'])
def form(username):
    if request.method == 'POST':
        height = request.form.get('height')
        weight = request.form.get('weight')
        bpm = request.form.get('bpm')
        oxy_sat = request.form.get('oxy_sat')
        tas = request.form.get('tas')
        tad = request.form.get('tad')
        #check info
        
        #if correct add to database
        medical_values = (height, weight, bpm, oxy_sat, tas, tad)
        database_functions.send_to_medicalinfo_db(medical_values,username)
        return redirect(url_for("report")) #renvoie l'utilisateur vers la page suivante

    return render_template("form.html")

@views.route("/page")
def page():
    args =request.args
    name = args.get('name') #/name=
    return render_template("index.html", name=name)


