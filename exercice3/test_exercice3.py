import unittest
import math
from exercice3.exercice_3 import sqrt


class TestSqrtFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(sqrt(9), 3.0)
        self.assertAlmostEqual(sqrt(16), 4.0)
        self.assertAlmostEqual(sqrt(1), 1.0)

    def test_zero(self):
        self.assertAlmostEqual(sqrt(0), 0.0)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            sqrt(-1)
        with self.assertRaises(ValueError):
            sqrt(-100)

    def test_non_integer_numbers(self):
        self.assertAlmostEqual(sqrt(2.25), 1.5)
        self.assertAlmostEqual(sqrt(0.25), 0.5)
