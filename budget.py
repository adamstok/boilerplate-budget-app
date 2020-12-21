class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        total_amount = sum([list(x.values())[0] for x in self.ledger])
        if total_amount - amount < 0:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True


def create_spend_chart(categories):
    pass
