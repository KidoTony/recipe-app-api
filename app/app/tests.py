from django.test import TestCase
from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Testing that 2 numbers are added together"""
        self.assertEqual(add(3, 5), 8)

    def test_subtract_numbers(self):
        """Testing that 2 numbers are subtract together"""
        self.assertEqual(subtract(5, 11), -6)
