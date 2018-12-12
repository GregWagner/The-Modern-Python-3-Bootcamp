class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, number):
        self.balance += number
        return self.balance

    def withdraw(self, number):
        self.balance -= number
        return self.balance
