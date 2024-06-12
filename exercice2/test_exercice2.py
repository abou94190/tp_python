import unittest
from exercice2.exercice_2 import Calculatrice


class TestCalculatrice(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calculatrice.addition(1, 2), 3)
        self.assertEqual(Calculatrice.addition(-1, 1), 0)
        self.assertEqual(Calculatrice.addition(-1, -1), -2)

    def test_soustraction(self):
        self.assertEqual(Calculatrice.soustraction(2, 1), 1)
        self.assertEqual(Calculatrice.soustraction(-1, -1), 0)
        self.assertEqual(Calculatrice.soustraction(1, -1), 2)

    def test_multiplication(self):
        self.assertEqual(Calculatrice.multiplication(2, 3), 6)
        self.assertEqual(Calculatrice.multiplication(-1, 1), -1)
        self.assertEqual(Calculatrice.multiplication(-1, -1), 1)

    def test_division(self):
        self.assertEqual(Calculatrice.division(6, 3), 2)
        self.assertEqual(Calculatrice.division(-1, 1), -1)
        self.assertEqual(Calculatrice.division(-1, -1), 1)
        self.assertEqual(Calculatrice.division(5, 2), 2.5)
        self.assertIsNone(Calculatrice.division(1, 0))


if __name__ == '__main__':
    unittest.main()
