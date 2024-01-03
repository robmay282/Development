import os
import pandas as pd 

class BankAccount:
    pass

    # _init_ Function
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []
        pass

    # # _str_
    def __str__(self):
        return f'Owner: {self.owner}\nOpening Balance: {self.balance}'

    # # deposit_funds()
    def deposit_funds(self, amount):
        t = {'owner': self.owner, 'type': 'deposit', 'amount': amount}
        self.transactions.append(t)
        
        print(self.transactions)

    # # withdraw_funds()
    # def __withdraw_funds__(self):
    #     pass

    # # get_balance()
    # def __get_balance__(self):
    #     pass

    # # get_transctions()
    # def __get_transctions__(self):
    #     pass

    # # transaction_count()
    # def __transaction_count__(self):
    #     pass

    # # transaction_history()
    # def __transaction_history__(self):
    #     pass

    # # save_transaction()
    # def __save_transaction__(self):
    #     pass

# create my class instance
my_bank_account = BankAccount('jean', 4000)
# testing __str__
print(my_bank_account)

#testing deposit
my_bank_account.deposit_funds(50)
my_bank_account.deposit_funds(200)