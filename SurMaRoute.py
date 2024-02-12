from flask import Blueprint, render_template, request, redirect, url_for
import database_functions, estcequejevaismourir_functions, getvalues_functions, graph_functions

views = Blueprint(__name__, "views")

# Login page
@views.route("/", methods = ['GET','POST']) # Allows for both 'GET' and 'POST' actions
def login():
    '''
    Function: login
    --------
    - Shows the login page
    - The user sends their username and password
    - If the user exists, redirect them to the medical form. If not, send an error message
    '''
    if request.method == 'POST': # Check for user input via a form element 
        username = request.form.get('username') # Collects the data wanted from the form 
        password = request.form.get('password')
        if database_functions.whoami(username) and password == database_functions.check_password(username): # Checks if valid username and password
            return redirect(url_for("SurMaRoute.form", username=username)) # Redirect to the medical form page
        else: 
            return render_template("login.html", message = "Nom d'utilisateur ou Mot de passe invalide!") # Error message if invalid
    return render_template("login.html") # Specifies the page displayed 

# Signup page
@views.route("/signup", methods = ['GET','POST']) # Allows for both 'GET' and 'POST' actions
def signup():
    '''
    Function: signup
    --------
    - Shows the signup page
    - The user fills up the form 
    - the user gets added to the database
    - the user is redirected to the login page
    '''
    if request.method == 'POST': # Check for user input via a form element
        # Collects the data from the form
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        sex = request.form.get('sex')=="M"
        birthday = request.form.get('birthday')
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        if database_functions.whoami(username): # Checks if user already exists
            return render_template("join-us.html", message = "Cet utilisateur existe déjà ! Si c'est vous, connectez-vous !")
        if password != password_confirm: # Check for valid password confirmation
            return render_template("join-us.html", message = "Veuillez confirmer votre mot de passe")
        database_functions.send_to_users_db(name,lastname,sex,birthday,username, password) # Add the new account to the database
        return redirect(url_for("SurMaRoute.login")) # Redirects to the login page
    return render_template("join-us.html")  # Specifies the page displayed 

# Form page
@views.route("/form/<username>", methods = ['GET','POST']) # Allows for both 'GET' and 'POST' actions
def form(username):
    '''
    Function: form
    --------
    - Shows the login page
    - The user fills up the medical form, Or can skip the form if wanted
    - The data is sent to the database
    - The user is redirected to the report page
    '''
    if database_functions.check_date(username): # Check if user has already filled the form today
        return redirect(url_for("SurMaRoute.report", username=username)) #send user to the report page
    if request.method == 'POST': # Check for user input via a form element 
        skipform = request.form.get('skipform')
        if skipform=="skipform":
            return redirect(url_for("SurMaRoute.report", username=username)) #send user to the report page
        else:
            # Collect data from the form 
            height = int(request.form.get('height'))
            weight = int(request.form.get('weight'))
            bpm = int(request.form.get('bpm'))
            oxy_sat = int(request.form.get('oxy_sat'))
            tas = int(request.form.get('tas'))
            tad = int(request.form.get('tad'))

            if tas < tad : # Checks for valid medical info
                return render_template("form.html", message = "La pression systolique doit etre plus élevé que la pression diastolique. Veuiller verifier vos valeurs")
            
            # Adds the new row to the database 
            medical_values = (height, weight, bpm, oxy_sat, tas, tad)
            database_functions.send_to_medicalinfo_db(medical_values,username)

            return redirect(url_for("SurMaRoute.report", username=username)) # Redirects user to the report page
    return render_template("form.html")  # Specifies the page displayed 

# Report page
@views.route("/report/<username>", methods = ['GET','POST']) # Allows for both 'GET' and 'POST' actions
def report(username):
    '''
    Function: report
    --------
    - Shows the report page
    - If the form was not filled up today, the user can go back to do it
    - Collects the user data from today and checks the values before showing the message on screen
    - Creates graph from all the values since account creation
    '''
    if request.method == 'POST': # Check for user input via a form element 
        takeform = request.form.get('takeform')
        if takeform=="takeform":
            return redirect(url_for("SurMaRoute.form", username=username)) # Redirects user to the form page
    
    if len(database_functions.watch_Le_JT_de_20H(username))==0: # Checks if the user has filled the form today
        bpm_message = imc_message = pressure_message = oxy_sat_message = "Vous n'avez pas rempli le formulaire aujoud'hui"
        message = "Vous n'avez pas rempli le formulaire aujourd'hui! Pour avoir un suivi personalisé, veuillez remplir le formulaire chaque jour."
        boolean = True
    else: # Collects the user's medical info from today
        message = ""
        boolean = False
        height,weight,bpm,oxy_sat,tas,tad, sex, birthday = database_functions.watch_Le_JT_de_20H(username)[0]
        age = getvalues_functions.get_age(birthday)

        # Checks the data 
        bpm_message = estcequejevaismourir_functions.ShakeItOff_bpm(bpm, sex, age)
        imc_message = estcequejevaismourir_functions.check_imc(getvalues_functions.get_imc(weight, height))
        pressure_message = estcequejevaismourir_functions.check_pressure(tas, tad)
        oxy_sat_message = estcequejevaismourir_functions.check_saturation(oxy_sat)


    # Errases the previous graphs before making new ones
        graph_functions.delete_allgraph()
    # Creates 4 Graphs
    bpm_image = graph_functions.bpm_graph(getvalues_functions.get_bpm_values(username))
    imc_image = graph_functions.imc_graph(getvalues_functions.get_imc_values(username))
    pressure_image = graph_functions.pressure_graph(getvalues_functions.get_pressure_values(username))
    oxy_sat_image = graph_functions.oxysat_graph(getvalues_functions.get_oxysat_values(username))

    # Collects user's name and last name to display a personalized message
    name,lastname = database_functions.get_name_lastname(username)
    welcome = "Bienvenue " + str(name) + " " + str(lastname) + "!"

    # Specifies the page displayed and sends the information displayed on the page 
    return render_template("report.html", bpmimage=bpm_image, bpmmessage=bpm_message, imcimage=imc_image, imcmessage=imc_message, pressureimage=pressure_image, pressuremessage= pressure_message, oxysatimage=oxy_sat_image, oxysatmessage=oxy_sat_message, welcome=welcome, message=message, boolean=boolean)

