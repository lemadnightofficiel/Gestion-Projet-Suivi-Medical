from flask import Blueprint, render_template, request, flash, redirect, url_for
import database_functions

views = Blueprint(__name__, "views")

# Login page
@views.route("/", methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print('password', password, "username", username, 'db password', database_functions.check_password(username))
        if database_functions.check_user(username) and password == database_functions.check_password(username):
            return redirect(url_for("views.form", username=username))
        else: 
            return render_template("login.html", message = "Invalid Username or Password")
    return render_template("login.html")

# Signup page
@views.route("/signup", methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        sex = request.form.get('sex')=="M"
        print(sex)
        birthday = request.form.get('birthday')
        username = request.form.get('username')
        password = request.form.get('password1')
        password_confirm = request.form.get('password2')
        if database_functions.check_user(username):
            return render_template("join-us.html", message = "User already exists! If this is you, go to the login page")
        if password != password_confirm:
            return render_template("join-us.html", message = "Please confirm your new password")
        database_functions.send_to_users_db(name,lastname,sex,birthday,username, password)
    return render_template("join-us.html")

# Form page
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
            return render_template("form.html", message = "La pression systolique doit etre plus élevé que la pression diastolique. Veuiller verifier vos valeurs")
        #if correct add to database
        medical_values = (height, weight, bpm, oxy_sat, tas, tad)
        database_functions.send_to_medicalinfo_db(medical_values,username)
        return redirect(url_for("views.report")) #renvoie l'utilisateur vers la page suivante
    return render_template("form.html")

# Report page
@views.route("/report")
def report():
    
    return render_template("report.html")

