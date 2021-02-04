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
        self.area = Circle.pi * radius * radius

    # DEFINE METHOD FOR RESETTING RADIUS
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = self.pi * new_radius * new_radius

    # DEFINE METHOD FOR CALCULATING CIRCUMFERENCE
    def getCircumference(self):
        return  2 * self.pi * self.radius

# CREATE AN INSTANCE OF A CIRCLE THROUGH THE CIRCLE CLASS
c = Circle()

# PRINT VALUES
print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())

# PRINT A SEPARATOR WITH A COMMENT
print('-----------------------')
print('Resetting the radius:')
# RESET THE RADIUS FOR THE INSTANCE
c.setRadius(2)

# PRINT VALUES FOR THE RESET INSTANCE
print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())
