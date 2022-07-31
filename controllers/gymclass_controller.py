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