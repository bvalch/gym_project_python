from flask import Flask,render_template,redirect,request
from flask import Blueprint
from models.member import Member
import repos.member_repo as member_repo
members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    return  'route test'