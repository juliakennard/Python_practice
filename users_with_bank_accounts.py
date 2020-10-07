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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .01, balance = 0) 

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

# Testing associated class and methods

julia = User(name = "Julia", email="julia@email.com")

julia.make_deposit(100).make_withdrawal(50).display_user_balance()



# SENSEI BONUS: Multiple accounts per users

class BankAccount2:
    def __init__(self, account_type, int_rate = .01, balance = 0):
        self.account_type = account_type
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

class User2:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account1 = BankAccount2(account_type = "checking", int_rate = .01, balance = 0) 
        self.account2 = BankAccount2(account_type = "savings", int_rate = .01, balance = 0) 

    def make_deposit(self, account_type, amount):
        if account_type == "checking":
            self.account1.deposit(amount)
        if account_type == "savings":
            self.account2.deposit(amount)
        return self

    def make_withdrawal(self, account_type, amount):
        if account_type == "checking":
            self.account1.withdraw(amount)
        if account_type == "savings":
            self.account2.withdraw(amount)
        return self

    def display_user_balance(self, account_type):
        if account_type == "checking":
            self.account1.display_account_info()
        if account_type == "savings":
            self.account2.display_account_info()
        return self

julia = User2("Julia", "julia@coding.com")

julia.make_deposit("checking",100).make_withdrawal("checking", 50).display_user_balance("checking")
julia.make_deposit("savings",500).make_withdrawal("savings", 100).display_user_balance("savings")