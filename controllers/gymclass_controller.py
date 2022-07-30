from flask import Flask,render_template,redirect,request
from flask import Blueprint
from models.gymclass import GymClass
import repos.gymclass_repo as gymclass_repo
gymclasses_blueprint = Blueprint("gymclasses", __name__)