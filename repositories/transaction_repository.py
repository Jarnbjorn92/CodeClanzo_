from db.run_sql import run_sql

from models.user import User
from models.transaction import Transaction

import repositories.user_repository as user_repository


def save(transaction):
    sql = "INSERT"