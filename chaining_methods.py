class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: " + str(self.name) + ", Balance: $" + str(self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

julia = User(name = "Julia", email="julia@email.com")

julia.make_deposit(100).make_withdrawal(50).display_user_balance()
