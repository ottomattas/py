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

# IMPORT MODULE
import name__one

# CALL METHOD FROM MODULE
name__one.func()

# CHECK IF SCRIPT IS BEING RUN DIRECTLY
# THROUGH BUILT-IN VARIABLE __name__
if __name__ == '__main__':

    # IF SCRIPT IS RAN DIRECTLY
    print('two.py is being run directly!')
else:

    # IF SCRIPT IS RAN THROUGH IMPORT
    print('two.py has been imported!')
