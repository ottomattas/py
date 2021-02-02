#!/usr/bin/env python
"""This is a simple class with some attributes
   to calculate area and circumference for a circle."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# DEFINE THE CIRCLE CLASS / OBJECT
class Circle:

    # DEFINE CLASS ATTRIBUTES
    pi = 3.14

    # CIRCLE IS INSTANTIATED (WITH A DEFAULT RADIUS)
    def __init__(self, radius=1):

        # DEFINE INSTANCE ATTRIBUTES
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # DEFINE METHOD FOR RESETTING RADIUS
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # DEFINE METHOD FOR CALCULATING CIRCUMFERENCE
    def getCircumference(self):
        return self.radius * self.pi * 2

# CREATE AN INSTANE OF A CIRCLE THROUGH THE CLASS
c = Circle()

# PRINT VALUES
print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())
