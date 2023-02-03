class Transaction:
    def __init__(self, merchant, category, amount, user, id = None):
        self.merchant = merchant
        self.category = category
        self.amount = amount
        self.user = user
        self.id = id