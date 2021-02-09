#!/usr/bin/env python
"""This is a simple method to capitalise text."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# DEFINE A METHOD TO CAPITALISE TEXT
def cap_text(text):
    '''
    Input a string
    Output a capitalised string
    '''

    # Upper case first letter
    #return text.capitalize()

    # Upper case first letter of every word
    return text.title()