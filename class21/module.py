import os
import pandas as pd 

class BankAccount:
    pass

    # _init_ Function
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

        pass

    # # _str_
    def __str__(self):
        return f'Owner: {self.owner}\nOpening Balance: {self.balance}'

    # # deposit_funds()
    # def __deposit_funds__(self):
    #     pass

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