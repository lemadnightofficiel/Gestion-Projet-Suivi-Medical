from flask import Blueprint, render_template, request, flash, redirect, url_for
import database_functions, checkvalues_functions, getvalues_functions, graph_functions

views = Blueprint(__name__, "views")

# Login page
@views.route("/", methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
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
        birthday = request.form.get('birthday')
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        if database_functions.check_user(username):
            return render_template("join-us.html", message = "User already exists! If this is you, go to the login page")
        if password != password_confirm:
            return render_template("join-us.html", message = "Please confirm your new password")
        database_functions.send_to_users_db(name,lastname,sex,birthday,username, password)
        return redirect(url_for("login.html", message="Account created successfully"))
    return render_template("join-us.html")

# Form page
@views.route("/form/<username>", methods = ['GET','POST'])
def form(username):
    if database_functions.check_date(username):
        return redirect(url_for("views.report", username=username)) #send user to next page
    if request.method == 'POST':
        skipform = request.form.get('skipform')
        if skipform=="skipform":
            return redirect(url_for("views.report", username=username)) #renvoie l'utilisateur vers la page suivante
        else:
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
            return redirect(url_for("views.report", username=username)) #renvoie l'utilisateur vers la page suivante
    return render_template("form.html")

# Report page
@views.route("/report/<username>", methods = ['GET','POST'])
def report(username):
    if request.method == 'POST':
        takeform = request.form.get('takeform')
        if takeform=="takeform":
            return redirect(url_for("views.form", username=username))
    
    if len(database_functions.get_today_info(username))==0:
        bpm_message,imc_message,pressure_message,oxy_sat_message = "Vous n'avez pas remplis le formulaire aujoud'hui"
        message = "Vous n'avez pas remplis le formulaire aujourd'hui! Pour avoir un suivi personalisé, veuillez remplir le formulaire chaque jour."
        boolean = True
    else:
        height,weight,bpm,oxy_sat,tas,tad, sex, birthday = database_functions.get_today_info(username)
        age = getvalues_functions.get_age(birthday)
        bpm_message = checkvalues_functions.check_bpm(bpm, sex, age)
        imc_message = checkvalues_functions.check_imc(getvalues_functions.get_imc(height, weight))
        pressure_message = checkvalues_functions.check_pressure(tas, tad)
        oxy_sat_message = checkvalues_functions.check_saturation(oxy_sat)

    bpm_image = graph_functions.bpm_graph(getvalues_functions.get_bpm_values(username))
    imc_image = graph_functions.imc_graph(getvalues_functions.get_imc_values(username))
    pressure_image = graph_functions.pressure_graph(getvalues_functions.get_pressure_values(username))
    oxy_sat_image = graph_functions.oxysat_graph(getvalues_functions.get_oxysat_values(username))

    name,lastname = database_functions.get_name_lastname(username)
    welcome = "Welcome" + str(name) + " " + str(lastname) + "!"
    return render_template("report.html", bpmimage=bpm_image, bpmmessage=bpm_message, imcimage=imc_image, imcmessage=imc_message, pressureimage=pressure_image, pressuremessage= pressure_message, oxysatimage=oxy_sat_image, oxysatmessage=oxy_sat_message, welcome=welcome, message=message, boolean=boolean)

