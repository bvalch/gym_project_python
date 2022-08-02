from flask import Flask,render_template,redirect,request
from flask import Blueprint
from models.member import Member
import repos.member_repo as member_repo
import repos.gymsession_repo as gymsession_repo
members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members=member_repo.select_all()
    return  render_template("/members/index.html", members=members)
    
@members_blueprint.route("/members/display/<id>")
def member(id):
    member=member_repo.select(id)
    return render_template("/members/show.html", member=member)

@members_blueprint.route("/members/new")
def new():
    return render_template("/members/new.html")

@members_blueprint.route("/members", methods=["POST"])
def new_member():
    name=request.form["name"]
    sex=request.form["gender"]
    new_member=Member(name,sex)
    member_repo.save(new_member)
    return redirect("/members")

@members_blueprint.route("/edit/<id>")
def edit(id):
    member=member_repo.select(id)
    return render_template("/members/edit.html",member=member)

@members_blueprint.route("/members/edit/<id>", methods=["POST"])
def edit_form(id):
    name=request.form["name"]
    sex=request.form["gender"]
    member=Member(name,sex,id)
    member_repo.update(member)
    return redirect("/members")

@members_blueprint.route("/edit/<id>/Deactivate")
def show_member_to_deactivate(id):
    member=member_repo.select(id)
    gymclasses=gymsession_repo.select(id)
    return render_template("/members/deactivate.html", member=member, gymclasses=gymclasses)

@members_blueprint.route("/edit/<id>/deactivate", methods=["POST"])
def deactivate_member(id):
    member=member_repo.select(id)
    gymsession_repo.deactivate(id)
    member_repo.update_deactivate(member)
    return redirect("/members")

@members_blueprint.route("/edit/<id>/Activate")
def show_member_to_activate(id):
    member=member_repo.select(id)
    return render_template("/members/activate.html",member=member)
    

@members_blueprint.route("/edit/<id>/activate",methods=["POST"])
def activate_member(id):
    member=member_repo.select(id)

    member_repo.update_activate(member)
    return redirect("/members")


