from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository
import repositories.transaction_repository as transaction_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route('/users')
def users():
    users = user_repository.select_all
    return render_template("users/index.html", all_users = users)

# NEW
# GET '/users/new'

# CREATE
# POST '/users'