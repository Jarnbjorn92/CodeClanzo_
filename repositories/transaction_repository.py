from db.run_sql import run_sql

from models.user import User
from models.transaction import Transaction

import repositories.user_repository as user_repository


def save(transaction):
    sql = "INSERT INTO transactions (merchant, category, amount, user_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [transaction.merchant, transaction.category, transaction.amount, transaction.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction


def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        transaction = Transaction(
            row['merchant'], 
            row['category'], 
            row['amount'],
            user,
            row['id'])
        transactions.append(transaction)
    return transactions


def delete_all():
    sql = "DELETE  FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)