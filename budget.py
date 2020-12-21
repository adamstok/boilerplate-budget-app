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

    def get_balance(self):
        total_amount = sum([list(x.values())[0] for x in self.ledger])
        return total_amount

    def transfer(self, amount, category_obj):
        ledger = category_obj.ledger
        total_amount = sum([list(x.values())[0] for x in self.ledger])
        if total_amount - amount < 0:
            return False
        else:
            transfer_to = f"Transfer to {category_obj.category}"
            self.ledger.append({"amount": -amount, "description": transfer_to})
            transfer_from = f"Transfer from {self.category}"
            ledger.append({"amount": amount, "description": transfer_from})
            return True


def create_spend_chart(categories):
    pass
