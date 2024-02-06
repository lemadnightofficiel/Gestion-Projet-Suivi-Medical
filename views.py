from flask import Blueprint, render_template, request, flash

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Tim")

@views.route("/profile/<username>")
def profile(username):
    args =request.args
    return render_template("index.html", name=username) 

@views.route("/page")
def page():
    args =request.args
    name = args.get('name') #/name=
    return render_template("index.html", name=name)

@views.route("/sendinfo" , methodes = ['GET','POST'])
def info():
    if request.method == 'POST':
        name = request.form.get('name')
        lastname = request.form.get('lastname')

        if len(name) <= 0:
            flash('Please input name', category='error')
        elif len(lastname) <= 0:
            flash('Please input last name', category='error')
        else:
            flash('yay name and lastname are valid!', category='success')
            #add to database
    return render_template("index.html")

