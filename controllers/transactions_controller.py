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
    users = user_repository.select_all()
    return render_template('transactions/new.html', transactions = transactions, all_users = users)

# CREATE
# POST '/transactions'
@transactions_blueprint.route('/transactions', methods = ['POST'])
def create_transaction():
    merchant = request.form['merchant']
    category = request.form['category']
    amount = request.form['amount']
    user = user_repository.select(request.form['user_id'])
    transaction = Transaction(merchant, category, amount, user)
    transaction_repository.save(transaction)
    return redirect('/transactions')

# SHOW
# GET '/transactions/<id>'

# EDIT
# GET '/transactions/<id>/edit'
@transactions_blueprint.route('/transactions/<id>/edit', methods = ['GET'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    users = user_repository.select_all()
    return render_template('transactions/edit.html', transaction = transaction, all_users = users)

# UPDATE
# PUT '/transactions/<id>'
@transactions_blueprint.route('/transactions/<id>', methods=['POST'])
def update_transaction(id):
    merchant = request.form['merchant']
    category = request.form['category']
    amount = request.form['amount']
    user = user_repository.select(request.form['user_id'])
    transaction = Transaction(merchant, category, amount, user, id)
    print(transaction.user.full_name)
    transaction_repository.update(transaction)
    return redirect('/transactions')

# DELETE
# DELETE '/transactions/<id>/delete'
@transactions_blueprint.route("/transactions/<id>/delete", methods = ['POST'])
def delete_book(id):
    transaction_repository.delete(id)
    return redirect('/transactions')