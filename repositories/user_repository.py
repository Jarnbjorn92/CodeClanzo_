from db.run_sql import run_sql

from models.user import User
from models.transaction import Transaction

def save(user):
    sql = "INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [user.first_name, user.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user


def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(
            row['first_name'],
            row['last_name'],
            row['id']
        )
        users.append(user)
    return users


def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user = User(result['first_name'], result['last_name'], result['id'] )
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(user):
    sql = "UPDATE users SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [user.id]
    run_sql(sql, values)


def transactions(user):
    transactions = []

    sql = "SELECT * FROM transactions WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        transaction = Transaction(
            row['merchant'],
            row['category'],
            row['amount'],
            row['user_id'],
            row['id']
        )
        transactions.append(transaction)
    return transactions