"""
Sample test
"""
from django.test import SimpleTestCase
from app.calc import add, substract


class CalcTest(SimpleTestCase):
    """The calc module"""

    def test_add_numbers(self):
        """Test adding two numbers together"""
        res = add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test subtracting two numbers"""
        res = substract(15, 10)
        self.assertEqual(res, 5)
