from random import randint

#defining the bankaccount class to put attributes and functions in
class BankAccount:
    routing_number = 123456789
    def __init__ (self, name):
        self.name = name
        self.account_number = randint(10000000, 99999999)
        self.balance = 0

    def deposit (self,amount):
        #+= automatically adds the inputed amount to our total balance
        self.balance += amount
        print(f'Thanks for depositing the amount of: ${amount}. To Bank of Ruot')

    def withdraw (self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Dont spend the amount of: ${amount}. all in one place ;)')
        else:
            self.balance -= 10
            print(f'Insufficient funds')


#Testing Init code
my_acc = BankAccount('Ruot')
print(my_acc.name)
print(my_acc.account_number)
print(my_acc.balance)
#-----------------------------
#Testing deposit and withdraw function
my_acc.deposit(20)
my_acc.withdraw(21)
print(my_acc.balance)