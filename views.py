from flask import Blueprint, render_template, request

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

