# Create a bank account class that stores an account holder's name and balance,
#  and implements methods to deposit money, withdraw money, and display the balance.
#  Don't want to lower withdrawal greater than the available balance.

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("Amount depoisted successfully !")

    def withdrawal(self,amount):
        if amount <= self.balance:
            self.balance =- amount
            print("Amount withdrawn successfully ")
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Holdername :",self.name)
        print("Account's Balance : ",self.balance)

name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, balance)

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)

account.display_balance()