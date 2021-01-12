#!/usr/bin/env python
"""This is a simple user input script."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# DEFINE THE USER CHOICE INPUT FUNCTION
def user_choice():
    
    # DEFINE VARIABLES
    choice = ' '
    within_range = False

    # KEEP ASKIGN FOR USER CHOICE INPUT
    while choice.isdigit() == False or within_range == False:
         
        choice = input('Please enter a number (0-10): ')
        
        # VALIDATE INPUT AS DIGIT
        if choice.isdigit() == False:
            print('Sorry, that is not a digit!')
        
        # VALIDATE INPUT RANGE
        if choice.isdigit() == True:
            if int(choice) in range(0,10):
                within_range = True
            else:
                within_range = False

    # RETURN THE USER CHOICE AS AN INT
    return int(choice)
    