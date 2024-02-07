from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Home")

@views.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", name="Dashboard")

@views.route("/report")
def report():
    return render_template("report.html", name="Report")