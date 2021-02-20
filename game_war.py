#!/usr/bin/env python
"""This is a simple simulated card game called War."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Testing"

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
        return self.rank + " of " + self.suit

# DECK CLASS

# PLAYER CLASS

##############
# GAME LOGIC #
##############