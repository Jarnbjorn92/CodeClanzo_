from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from models.user import User
import repositories.user_repository as user_repository
import repositories.transaction_repository as transaction_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route('/transactions')
def show_transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", all_transactions = transactions)

# NEW
# GET '/transactions/new'
@transactions_blueprint.route("/transactions/new")
def new_transaction():
    transactions = transaction_repository.select_all()
    return render_template('transactions/new.html', transactions = transactions)

# CREATE
# POST '/transactions'



# SHOW
# GET '/transactions/<id>'

# EDIT
# GET '/transactions/<id>/edit'

# UPDATE
# PUT '/transactions/<id>'

# DELETE
# DELETE '/transactions/<id>/delete'
@transactions_blueprint.route("/transactions/<id>/delete", methods = ['POST'])
def delete_book(id):
    transaction_repository.delete(id)
    return redirect('/transactions')