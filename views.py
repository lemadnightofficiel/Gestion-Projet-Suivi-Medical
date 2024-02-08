from flask import Blueprint, render_template, request, flash

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Home")

@views.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", name="Dashboard")

@views.route("/page")
def report():
    args =request.args
    name = args.get('name') #/name=
    return render_template("index.html", name=name)

