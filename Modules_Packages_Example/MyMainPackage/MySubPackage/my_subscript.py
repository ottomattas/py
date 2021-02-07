#!/usr/bin/env python
"""This is a simple subpackage."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# DEFINE METHOD FOR PRINTING AN INFORMATIONAL
def sub_report():
    print('Hey, I\'m a method in ./MyMainPackage/SubPackage/' + '\033[1m' + 'my_subscript.py' + '\033[0m' + '.')