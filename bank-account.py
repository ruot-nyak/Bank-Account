from random import randint

#defining the bankaccount class to put attributes and functions in
class BankAccount:
    def __init__ (self, name):
        self.name = name
        self.account_number = randint(10000000, 99999999)
        self.balance = 0
        self.routing_number = 123456789

    def atm_fee (self):
        self.balance -= 2

    def deposit (self,amount):
        #+= automatically adds the inputed amount to our total balance
        self.balance += amount
        print(f'Thanks for depositing the amount of: ${amount}. To Bank of Ruot')

    def withdraw (self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.atm_fee()
            print(f'Dont spend the amount of: ${amount}. all in one place ;). Enjoy our $2 atm fee!')
        else:
            self.balance -= 10
            print(f'Insufficient funds')

    def get_balance (self):
        print(f'You have the balance of: ${self.balance}.')
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += round(interest, 2)

    def print_receipt(self):
        print(f' {self.name}\n Account No: ****{str(self.account_number)[4:]}\n Routing No: {self.routing_number}\n Balance: {self.balance}')

        


#Testing Init code
my_acc = BankAccount('Ruot')
print(my_acc.name)
print(my_acc.account_number)
print(my_acc.balance)
print(my_acc.routing_number)

print('-----------------------------')
#Testing deposit and withdraw function
my_acc.deposit(20)
my_acc.withdraw(21)
print(my_acc.balance)

print('-----------------------------')
#testing get_balance
my_acc.get_balance()

print('-------------------------------')
#printing receipt
my_acc.print_receipt()