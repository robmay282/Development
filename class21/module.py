import os
import pandas as pd 

class BankAccount:
    pass

    # _init_ Function
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []
       

    # # _str_
    def __str__(self):
        return f'Owner: {self.owner}\nOpening Balance: {self.balance}'

    # # deposit_funds()
    def deposit_funds(self, amount):
        t = {'owner': self.owner, 'type': 'deposit', 'amount': amount}
        self.transactions.append(t)
        return self.transactions
        #print(self.transactions)

    # # withdraw_funds()
    def withdraw_funds(self, amount):
        t = {'owner': self.owner, 'type': 'withdrawal', 'amount': amount}
        self.transactions.append(t)
        print(self.transactions)
       

    # # get_balance()
    # def get_balance(self):
    #     pass

    # # get_transctions()
    # def get_transctions(self):
    #     pass

    # # transaction_count()
    # def transaction_count(self):
    #     pass

    # # transaction_history()
    # def transaction_history(self):
    #     pass

    # # save_transaction()
    # def save_transaction(self):
    #     pass

# create my class instance
jeans_account = BankAccount('jean', 4000)
majestic_account = BankAccount('majestic', 5000)
# testing __str__
# print(jeans_account)

#testing deposit
jeans_account.deposit_funds(50)
jeans_account.deposit_funds(200)
majestic_account.deposit_funds(200)

#testing withdraw
jeans_account.withdraw_funds(25)
jeans_account.withdraw_funds(100)
jeans_account.withdraw_funds(50)