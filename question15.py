"""
Imagine you are designing a bank application. 
what would a customer look like? What attributes 
would she have? What methods would she have?
"""

class  Customer():
    
    def __init__(self, account_no, name, address, email, balance):
        self.account_no = account_no
        self.name = name
        self.address = address
        self.email = email
        self.balance = balance

    def get_balance(self):
        return self.balance

    def add_balance(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance = self.balance - amount
