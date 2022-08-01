from flask import Flask,render_template,redirect,request
from flask import Blueprint
from models.gymsession import Gymsession
import repos.gymsession_repo as gymsession_repo
gymsessions_blueprint = Blueprint("gymsessions", __name__)

@gymsessions_blueprint.route("/gymsessions")
def show_all():
    gymsessions=gymsession_repo.select_all()
    return render_template("/gymsessions/index.html", gymsessions=gymsessions)