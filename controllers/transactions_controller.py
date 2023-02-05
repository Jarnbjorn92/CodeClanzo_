from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.user_repository as user_repository
import repositories.transaction_repository as transaction_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route('/transactions/index.html')
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", all_transactions = transactions)

# NEW
# GET '/transactions/new'

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
    