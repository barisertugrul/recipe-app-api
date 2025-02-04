"""
Sample test cases for the app
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test cases for the calc module """

    def test_add(self):
        """ Test adding numbers together """
        # self.assertEqual(calc.add(3, 8), 11)
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
    
    def test_subtract(self):
        """ Test subtracting numbers """
        res = calc.subtract(10, 15)
        self.assertEqual(res, -5)