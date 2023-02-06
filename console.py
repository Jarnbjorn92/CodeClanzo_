from models.user import User
from models.transaction import Transaction

import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

user_1 = User('Connor', 'Fleming')
user_repository.save(user_1)

# TESTED AND WORKS. 

# user_repository.delete(1)
# TESTED AND WORKS.


transaction_1 = Transaction("ASDA", "Groceries", 10.50, user_1)
transaction_repository.save(transaction_1)

users = user_repository.select_all()

# TESTED AND WORKS

# transaction_repository.select_all()
# transaction_repository.delete(2)
# TESTED AND WORKING

# transaction_repository.select(1)
# user_repository.select_all()
