# CodeClanzo - Spending Tracker

## Brief:

###Spending Tracker
Build an app that allows a user to track their spending.

### MVP
⋅⋅* The app should allow the user to create and edit merchants, e.g. Tesco, Amazon, ScotRail
⋅⋅* The app should allow the user to create and edit tags for their spending, e.g. groceries, entertainment, transport
⋅⋅* The user should be able to assign tags and merchants to a transaction, as well as an amount spent on each transaction.
⋅⋅* The app should display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.

### Possible Extensions
⋅⋅* The user should be able to mark Merchants and Tags as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction.
⋅⋅* Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
⋅⋅* The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.
⋅⋅* The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.


## To Run File:
1. dropdb -d codeclanzo_manager 
2. createdb -d codeclanzo_manager
3. psql -codeclanzo_manager -f codeclanzo_manager.sql
4. python3 console.py (optional to populate DB with a user and a transaction)
5. flask run (click IP address for homepage)


## User instructions:

### User
⋅⋅* To create user, go to the 'User' section. Input users first and last name in before hitting 'Create'.
⋅⋅* By clicking the user you can view the total amount spent, and transactions related to that user.

### Transactions
⋅⋅* To create a new transaction, use the 'New Transaction' menu option. Add details and hit confirm. Any created users will appear in the user section.
⋅⋅* To see all and edit transactions, go to the 'All Transactions' menu option. From here you can delete and/or update transactions.
