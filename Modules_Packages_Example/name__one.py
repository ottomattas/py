#!/usr/bin/env python
"""This is a simple script for explaining
the built-in __name__ variable."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# DEFINE METHOD FOR PRINTING AN INFORMATIONAL
def func():
    print('func() in one.py')

# CHECK IF SCRIPT IS BEING RUN DIRECTLY
# THROUGH BUILT-IN VARIABLE __name__
if __name__ == '__main__':

    # IF SCRIPT IS RAN DIRECTLY
    print('one.py is being run directly!')
else:

    # IF SCRIPT IS RAN THROUGH IMPORT
    print('one.py has been imported!')
