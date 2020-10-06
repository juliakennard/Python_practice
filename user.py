# Creating a class

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User: " + str(self.name) + ", Balance: $" + str(self.account_balance))

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

# Creating 3 instances

julia = User(name = "Julia Busso", email="julia@email.com")
john = User(name = "John Busso", email="julia@email.com")
mila = User(name = "Mila Busso", email="julia@email.com")

print(julia.account_balance)

# Testing methods

julia.make_deposit(100)
julia.make_deposit(50)
julia.make_deposit(20)
julia.make_withdrawal(50)
julia.display_user_balance()

john.make_deposit(500)
john.make_deposit(200)
john.make_withdrawal(300)
john.make_withdrawal(500)
john.display_user_balance()

mila.make_deposit(100)
mila.make_withdrawal(10)
mila.make_withdrawal(10)
mila.make_withdrawal(20)
mila.display_user_balance()

# BONUS: Testing transfer method

julia.transfer_money(other_user = john, amount = 100)

print(julia.account_balance)
print(john.account_balance)


    

    

