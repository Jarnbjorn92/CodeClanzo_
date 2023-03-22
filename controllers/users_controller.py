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

# TO SHOW USER WITH TOTAL TRANSACTION AMOUNT
# GET ROUTE TO USERS SPECIFIC ID 
# USER VARIABLE ASSIGNED BY A SELECT USER METHOD THAT LOOKS THROUGH THE DATABASE FOR SPECIFIC USER ID.
# TRANSACTION VARIABLE ASSIGNED BUY LOOKING THOUGH THE USER DATABASE FOR ALL TRANSACTIONS LINKED TO SPECIFIC USER ID
# TOTAL OF TRANSACTION DISPLAYED BY FINDING THE SUM OF ALL ASSOCIATED TRANSACTIONS TO THE SPECIFIC USER
@users_blueprint.route('/users/<id>')
def show_user(id):
    user = user_repository.select(id)
    transactions = user_repository.transactions(user)
    total = user.get_total(transactions)

    return render_template('/users/show.html', user = user, user_transactions = transactions, user_total = total)

# DELETE
# POST '/users/<id>/delete
@users_blueprint.route('/users/<id>/delete', methods=['POST'])
def delete_user(id):
    user_repository.delete(id)
    return redirect('/users')