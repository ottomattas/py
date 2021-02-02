#!/usr/bin/env python
"""This is a simple class with some attributes
   to show class inheritance."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# DEFINE THE ANIMAL BASE CLASS / OBJECT
class Animal:

    # ANIMAL IS INSTANTIATED
    def __init__(self):
        print("Animal created")

    # DEFINE A CLASS METHOD FOR IDENTIFYING SELF
    def whoAmI(self):
        print("Animal")

    # DEFINE A CLASS METHOD FOR EATING
    def eat(self):
        print("Eating")

# DEFINE THE DOG CLASS / OBJECT
class Dog(Animal):

    # DOG IS INSTANTIATED WITH INHERITED ATTRIBUTES FROM BASE CLASS
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    # OVERWRITE THE BASE CLASS METHOD DEFINITION FOR IDENTIFYING SELF
    def whoAmI(self):
        print("Dog")

    # DEFINE A CLASS METHOD FOR BARKING
    def bark(self):
        print("Woof!")

# CREATE AN INSTANCE OF A DOG THROUGH THE DOG CLASS
d = Dog()

# CALL OVERWRITTEN CLASS METHOD
d.whoAmI()

# CALL INHERITED CLASS METHOD
d.eat()

# CALL CLASS METHOD
d.bark()
