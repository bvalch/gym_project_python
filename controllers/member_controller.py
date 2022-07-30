from flask import Flask,render_template,redirect,request
from flask import Blueprint
from models.member import Member
import repos.member_repo as member_repo
members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members=member_repo.select_all()
    return  render_template("/members/index.html", members=members)