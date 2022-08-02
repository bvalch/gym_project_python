from flask import Flask,render_template,redirect,request
from flask import Blueprint
from models.gymsession import Gymsession
from models.gymclass import GymClass
import repos.gymclass_repo as gymclass_repo
import repos.member_repo as member_repo
import repos.gymsession_repo as gymsession_repo
gymclasses_blueprint = Blueprint("gymclasses", __name__)

@gymclasses_blueprint.route("/classes")
def gymclasses_show():
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
def edit_form(id):
    name=request.form["name"]
    capacity=request.form["capacity"]
    gym_active=request.form["gym_active"]
    gymclass=GymClass(name,capacity,gym_active,id)
    gymclass_repo.update(gymclass)
    gymclass=gymclass_repo.select(id)
    if gymclass.gym_active==False:
        gymclass_repo.deactivate_members(id)
    
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

@gymclasses_blueprint.route("/classes/<id>/add")
def add_template(id):
    gymclass=gymclass_repo.select(id)
    members=member_repo.select_all()
    gymsession=gymsession_repo.show_attendees(id)
    return render_template("gymclasses/add.html", gymclass=gymclass, members=members,gymsession=gymsession)

@gymclasses_blueprint.route("/classes/<id>/add", methods=["POST"])
def add_member(id):
    members_id=request.form.getlist("member_id")
    members=[]
    for item in members_id:
            members.append(member_repo.select(item))
    if gymsession_repo.get_capacity(id,members):
        gymclass=gymclass_repo.select(id)
        gymsession=Gymsession(members,gymclass)
        gymsession_repo.save(gymsession)
        return redirect("/classes")
    else:
        return 'error'

@gymclasses_blueprint.route("/gymsession/<id>/attending")
def show_attending(id):
    attendees = gymsession_repo.show_attendees(id)
    return render_template("/gymsessions/attending.html",attendees=attendees)
