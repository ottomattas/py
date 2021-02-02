#!/usr/bin/env python
"""This is a simple class with some attributes
   and magic methods."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# DEFINE THE BOOK CLASS / OBJECT
class Book:

    # BOOK IS INSTANTIATED
    def __init__(self, title, author, pages):
        print("A book is created")

        # DEFINE INSTANCE ATTRIBUTES
        self.title = title
        self.author = author
        self.pages = pages

    # DEFINE MAGIC METHOD FOR STRING REPRESENTATION
    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    # DEFINE MAGIC METHOD FOR LENGTH FOR USER DEFINED OBJECTS
    def __len__(self):
        return self.pages

    # DEFINE MAGIC METHOD FOR DELETE KEY
    def __del__(self):
        print("A book is destroyed")

# CREATE AN INSTANCE OF A BOOK THROUGH THE BOOK CLASS
book = Book("Python Rocks!", "Jose Portilla", 159)

# SHOW MAGIC METHODS IN ACTION #
################################

# STRING MAGIC
print(book)

# LENGHT MAGIC
print(len(book))

# DEL KEY MAGIC
del book