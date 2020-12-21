class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_founds(amount) == False:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True

    def get_balance(self):
        total_amount = sum([list(x.values())[0] for x in self.ledger])
        return total_amount

    def transfer(self, amount, category_obj):
        ledger = category_obj.ledger
        if self.check_founds(amount) == False:
            return False
        else:
            transfer_to = f"Transfer to {category_obj.category}"
            self.ledger.append({"amount": -amount, "description": transfer_to})
            transfer_from = f"Transfer from {self.category}"
            ledger.append({"amount": amount, "description": transfer_from})
            return True

    def check_founds(self, amount):
        total_amount = sum([list(x.values())[0] for x in self.ledger])
        if amount > total_amount:
            return False
        else:
            return True

    def total_withdraws(self):
        withdraws = rount(sum([x["amount"]
                               for x in self.ledger if x["amount"] < 0]), 2)
        return withdraws

    def __str__(self):
        head_middle = (30 - len(self.category)) // 2
        head = '*' * head_middle + self.category + '*' * head_middle
        print(head)
        total_amount = sum([list(x.values())[0] for x in self.ledger])
        for el in self.ledger:
            description = el["description"][:24]
            amount = '%.2f' % el["amount"]
            fill = len(head) - len(description) - len(amount)
            body = description + (' ' * fill) + amount
            print(body)
        print(f"Total: {total_amount}")


def create_spend_chart(categories):
    percent = {}
    for el in categories:
        percent[el.category] = el.total_withdraws()
