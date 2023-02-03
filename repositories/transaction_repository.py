from db.run_sql import run_sql

from models.user import User
from models.transaction import Transaction

import repositories.user_repository as user_repository


def save(transaction):
    sql = "INSERT INTO transactions (merchant, category, amount, user_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [
        transaction.merchant,
        transaction.category,
        transaction.amount,
        transaction.user.id
        ]
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


def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user = user_repository.select(result['user_id'])
        transaction = Transaction(
            result['merchant'],
            result['category'],
            result['amount'], 
            user, 
            result['id']
            )
    return transaction


def delete_all():
    sql = "DELETE  FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(transaction):
    sql = "UPDATE transactions SET (merchant, category, amount, user_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [
        transaction.merchant, 
        transaction.category, 
        transaction.amount, 
        transaction.user.id, 
        transaction.id
        ]
    run_sql(sql, values)