from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository
import repositories.transaction_repository as transaction_repository

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route('/users')
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", all_users = users)

# CREATE
# POST '/users'
@users_blueprint.route('/users', methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    user = User(first_name,last_name)
    user_repository.save(user)
    return redirect('/users')

# SHOW
# GET '/users/<id>'
# ALSO HAS TO SHOW TRANSACTIONS
@users_blueprint.route('/users/<id>')
def show_user(id):
    user = user_repository.select(id)

    return render_template('/users/show.html', user = user)


# DELETE
# POST '/users/<id>/delete
@users_blueprint.route('/users/<id>/delete', methods=['POST'])
def delete_user(id):
    user_repository.delete(id)
    return redirect('/users')