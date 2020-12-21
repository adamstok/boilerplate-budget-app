class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True

    def get_balance(self):
        total_amount = sum([list(x.values())[0] for x in self.ledger])
        return total_amount

    def transfer(self, amount, category_obj):
        ledger = category_obj.ledger
        if self.check_funds(amount) == False:
            return False
        else:
            transfer_to = f"Transfer to {category_obj.category}"
            self.ledger.append({"amount": -amount, "description": transfer_to})
            transfer_from = f"Transfer from {self.category}"
            ledger.append({"amount": amount, "description": transfer_from})
            return True

    def check_funds(self, amount):
        total_amount = sum([list(x.values())[0] for x in self.ledger])
        if amount > total_amount:
            return False
        else:
            return True

    def total_withdraws(self):
        withdraws = round(sum([x["amount"]
                               for x in self.ledger if x["amount"] < 0]), 2)
        return withdraws

    def __str__(self):
        head_middle = (30 - len(self.category)) // 2
        head = '*' * head_middle + self.category + '*' * head_middle
        print(head)
        total_amount = sum([list(x.values())[0] for x in self.ledger])
        for el in self.ledger:
            description = el["description"][:23]
            amount = '%.2f' % el["amount"]
            fill = len(head) - len(description) - len(amount)
            body = description + (' ' * fill) + amount
            print(body)
        print(f"Total: {total_amount}")


def create_spend_chart(categories):
    total_withdraws = 0
    percent = {}
    for el in categories:
        total_withdraws += el.total_withdraws()
    for el in categories:
        p1 = total_withdraws / el.total_withdraws()
        p2 = 100 // p1
        percent[el.category] = p2
    print(percent)
    outp = sl(percent)
    return outp


def sl(x):
    total_len = 5 + (len(x) * 2)
    output_list = ['Percentage spent by category']
    max_deep = 0
    xx = []
    for i in x:
        xx.append(list(i))
    st = ''
    for i in range(10, -1, -1):
        s = f'{i * 10}'.rjust(3, ' ')+'| '
        for p in x.values():
            if p >= i * 10:
                s += 'o  '
            else:
                s += '   '
        if len(s) <= 5:
            s = s.ljust(total_len)
        output_list.append(s)
    bottom = '-' * (len(s) - 4)
    bottom = bottom.rjust(total_len, ' ')
    output_list.append(bottom)
    for i in x:
        max_deep = max(max_deep, len(i))
    for i in range(max_deep):
        for j in xx:
            if i <= len(j) - 1:
                st += j[i] + '  '
            else:
                st += ' ' + '  '
            if j == xx[-1]:
                st = st.rjust(total_len, ' ')
                output_list.append(st)
                st = ''
    print('\n'.join(output_list))
    return '\n'.join(output_list)
