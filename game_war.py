#!/usr/bin/env python
"""This is a simple simulated card game called War."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Testing"

####################
# GLOBAL VARIABLES #
####################

# DEFINE VALUES DICT FOR GIVING THE RANK A VALUE
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,
        'Seven':7,'Eight':8,'Nine':9,'Ten':10,
        'Jack':11,'Queen':12,'King':13,'Ace':14}

#####################
# CLASS DEFINITIONS #
#####################

# CARD CLASS
class Card():

    # CARD IS INSTANTIATED WITH SUIT AND RANK
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    # DEFINE A STRING METHOD TO HELP HUMAN UNDERSTAND THE CARD
    def __str__(self):
        return self.rank + ' of ' + self.suit


# DECK CLASS

# PLAYER CLASS

##############
# GAME LOGIC #
##############