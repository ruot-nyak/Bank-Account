from random import randint

#defining the bankaccount class to put attributes and functions in
class BankAccount:
    def __init__ (self, name):
        self.name = name
        self.account_number = randint(10000000, 99999999)
        self.balance = 100

#Testing Init code
my_acc = BankAccount('Ruot')
print(my_acc.name)
print(my_acc.account_number)
print(my_acc.balance)