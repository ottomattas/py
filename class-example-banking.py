#!/usr/bin/env python
"""This is a simple bank account class
with some attributes and methods to manipulate it."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

#####################
# CLASS DEFINITIONS #
#####################

# DEFINE THE ACCOUNT CLASS / OBJECT
class Account:

    # ACCOUNT IS INSTANTIATED (WITH DEFAULT BALANCE)
    def __init__(self, owner, balance=0):

        # DEFINE INSTANCE ATTRIBUTES
        self.owner = owner
        self.balance = balance

    # DEFINE METHOD FOR DEPOSITING
    def deposit(self, amount):
    
        # ADD AMOUNT TO BALANCE
        self.balance = self.balance + amount

        # PRINT OUT A MESSAGE WITH NEW BALANCE STATEMENT
        print(f'Deposit accepted! New balance: {self.balance}')

    # DEFINE METHOD FOR WITHDRAWING
    def withdraw(self, amount):

        # CHECK FOR ENOUGH BALANCE TO WITHDRAW
        if amount <= self.balance:

            # REDUCE AMOUNT FROM BALANCE
            self.balance = self.balance - amount

            # PRINT OUT A MESSAGE WITH NEW BALANCE STATEMENT
            print(f'Withdrawal successful! New balance: {self.balance}')

        # BALANCE IS NOT ENOUGH TO WITHDRAW
        else:
            # PRINT OUT A MESSAGE WITH NEW BALANCE STATEMENT
            print(f'Sorry, not enough funds! Current balance: {self.balance}')

    # DEFINE METHOD FOR RETURNING ACCOUNT INFORMATION
    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'

######################################
# CREATE INSTANCES AND PRINT RESULTS #
######################################

# CREATE INSTANCES OF ACCOUNTS THROUGH THE ACCOUNT CLASS
account1 = Account('Bob',100)
account2 = Account('Bill')

# PRINT A SEPARATOR WITH A COMMENT
print()
print('-----------------------')
print('ACCOUNT 1')
print('-----------------------')
# PRINT VALUES
print(account1)
print('-')
print('-')
print(account1)

# PRINT A SEPARATOR WITH A COMMENT
print()
print('-----------------------')
print('ACCOUNT 2')
print('-----------------------')
print(account2)
print('-')
print('-')
print(account2)
