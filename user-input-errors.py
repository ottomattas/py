#!/usr/bin/env python
"""This is a simple user input function
to demonstrate error handling."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# DEFINE THE USER CHOICE INPUT FUNCTION
def getNumber():

    # KEEP ASKING FOR VALID INPUT
    while True:

        # TRY TO CONVERT THE INPUT TO INT
        try:
            a = int(input('Enter a number: '))

        # THROW AN EXCEPTION
        except:
            print('This is not a valid number. Try again.')
            continue

        # BREAK OUT WHEN VALID NUMBER IS GIVEN
        else:
            break
