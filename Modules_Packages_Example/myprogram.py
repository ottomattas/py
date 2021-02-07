#!/usr/bin/env python
"""This is a simple program to show examples
on how to use modules and packages."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# IMPORT METHOD FROM MODULE
from mymodule import my_func

# CALL THE METHOD
my_func()
print('-----------')

# IMPORT MAIN PACKAGE
from MyMainPackage import my_main_script

# CALL METHOD FROM MAIN PACKAGE
my_main_script.report_main()
print('-----------')
