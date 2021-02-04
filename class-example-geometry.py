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

#####################
# CLASS DEFINITIONS #
#####################

# DEFINE THE CIRCLE CLASS / OBJECT
class Circle:

    # DEFINE CLASS ATTRIBUTES
    pi = 3.14

    # CIRCLE IS INSTANTIATED (WITH A DEFAULT RADIUS)
    def __init__(self, radius=1):

        # DEFINE INSTANCE ATTRIBUTES
        self.radius = radius 
        self.area = Circle.pi * radius ** 2

    # DEFINE METHOD FOR RESETTING RADIUS
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = Circle.pi * new_radius ** 2

    # DEFINE METHOD FOR CALCULATING CIRCUMFERENCE
    def getCircumference(self):
        return  2 * Circle.pi * self.radius

# DEFINE THE CYLINDER CLASS / OBJECT
class Cylinder:
    
    # DEFINE CLASS ATTRIBUTES
    pi = 3.14

    # CYLINDER IS INSTANTIATED (WITH A DEFAULT HEIGHT AND RADIUS)
    def __init__(self,height=1,radius=1):

        # DEFINE INSTANCE ATTRIBUTES
        self.height = height
        self.radius = radius

    # DEFINE METHOD FOR CALCULATING VOLUME  
    def volume(self):
        return Cylinder.pi * self.radius ** 2 * self.height
    
    # DEFINE METHOD FOR CALCULATING SURFACE AREA
    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * (self.height + self.radius)

# DEFINE THE LINE CLASS / OBJECT
class Line:
    
    # LINE IS INSTANTIATED (WITH TWO COORDINATES)
    def __init__(self,coor1,coor2):

        # DEFINE INSTANCE ATTRIBUTES
        self.coor1 = coordinate1
        self.coor2 = coordinate2
    
    # DEFINE METHOD FOR CALCULATING DISTANCE
    def distance(self):

        # DEFINE LINE COORDINATES
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        # RETURN DISTANCE
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # DEFINE METHOD FOR CALCULATING SLOPE
    def slope(self):

        # DEFINE LINE COORDINATES
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        # RETURN SLOPE
        return (y2 - y1) / (x2 - x1)

######################################
# CREATE INSTANCES AND PRINT RESULTS #
######################################

##########
# CIRCLE #
##########
# CREATE AN INSTANCE OF A CIRCLE THROUGH THE CIRCLE CLASS
circle = Circle()

# PRINT A SEPARATOR WITH A COMMENT
print()
print('-----------------------')
print('Circle calculations')
# PRINT VALUES
print('Radius is: ',circle.radius)
print('Area is: ',circle.area)
print('Circumference is: ',circle.getCircumference())

# PRINT A SEPARATOR WITH A COMMENT
print('-----------------------')
print('Resetting the circle radius')
# RESET THE RADIUS FOR THE INSTANCE
circle.setRadius(2)

# PRINT VALUES FOR THE RESET INSTANCE
print('New radius is: ',circle.radius)
print('New area is: ',circle.area)
print('New circumference is: ',circle.getCircumference())

############
# CYLINDER #
############
# CREATE AN INSTANCE OF A CYLINDER THROUGH THE CYLINDER CLASS
cylinder = Cylinder(2,3)

# PRINT A SEPARATOR WITH A COMMENT
print()
print('-----------------------')
print('Cylinder calculations')
# PRINT VALUES
print('Volume is: ',cylinder.volume())
print('Surface area is: ',cylinder.surface_area())

############
# LINE #
############
# CREATE AN INSTANCE OF A LINE THROUGH THE LINE CLASS
coordinate1 = (3,2)
coordinate2 = (8,10)

line = Line(coordinate1,coordinate2)

# PRINT A SEPARATOR WITH A COMMENT
print()
print('-----------------------')
print('Line calculations')
# PRINT VALUES
print('Distance is: ',line.distance())
print('Slope is: ',line.slope(),'degrees')
