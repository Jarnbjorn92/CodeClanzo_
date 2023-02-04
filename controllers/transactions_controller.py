from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.user_repository as user_repository
import repositories.transaction_repository as transaction_repository

transactions_blueprint = Blueprint("transactions", __name__)


# NEW
# GET '/users/new'

# CREATE
# POST '/users'

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
# DELETE '/transactions/<id>'
