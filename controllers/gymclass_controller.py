from flask import Flask,render_template,redirect,request
from flask import Blueprint
from models.gymclass import GymClass
import repos.gymclass_repo as gymclass_repo
gymclasses_blueprint = Blueprint("gymclasses", __name__)

@gymclasses_blueprint.route("/classes")
def gymclasses():
    gymclasses=gymclass_repo.select_all()
    return render_template("/gymclasses/index.html", gymclasses=gymclasses)

@gymclasses_blueprint.route("/classes/<id>")
def show(id):
    gymclass=gymclass_repo.select(id)
    return render_template("gymclasses/show.html",gymclass=gymclass)

@gymclasses_blueprint.route("/classes/<id>/edit")
def edit(id):
    gymclass=gymclass_repo.select(id)
    return render_template("/gymclasses/edit.html", gymclass=gymclass)

@gymclasses_blueprint.route("/classes/<id>/edit", methods=["POST"])
def edit_for(id):
    name=request.form["name"]
    capacity=request.form["capacity"]
    gymclass=GymClass(name,capacity,id)
    gymclass_repo.update(gymclass)
    return redirect("/classes")

@gymclasses_blueprint.route("/classes/new")
def new_class():
    return render_template("gymclasses/new.html")

@gymclasses_blueprint.route("/new/create", methods=["POST"])
def create():
    name=request.form["name"]
    capacity=request.form["capacity"]
    gymclass=GymClass(name,capacity)
    gymclass_repo.save(gymclass)

    return redirect("/classes")