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
