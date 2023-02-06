class User:
    def __init__(self, first_name, last_name, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_total(self, transactions):
        total = 0

        for transaction in transactions:
            total += transaction.amount

        return total