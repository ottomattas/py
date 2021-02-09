#!/usr/bin/env python
"""This is a simple unittest 
to check for capitalisation method."""

__author__ = "Otto Mättas"
__copyright__ = "Copyright 2021, The Python Problems"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Otto Mättas"
__email__ = "otto.mattas@eesti.ee"
__status__ = "Development"

# IMPORT MODULES
import unittest
import capitalise as cap

# CREATE A CLASS TO BE CALLED AT THE END
class TestCap(unittest.TestCase):

    # CREATE A METHOD TO BE CALLED TO TEST ONE WORD
    def test_one_word(self):

        # DEFINE A VARIABLE
        text = 'python'

        # CALL A METHOD FROM IMPORTED SCRIPT
        result = cap.cap_text(text)

        # CHECK IF RESULT IS AS EXPLICITLY ASSRTED
        self.assertEqual(result, 'Python')

