# Create class BankAccount

class BankAccount:
    def __init__(self, int_rate = .01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount <0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else: 
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

# Create two accounts

account1 = BankAccount()
account2 = BankAccount(.05, 100)

account1.deposit(100).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()
account2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).display_account_info()
