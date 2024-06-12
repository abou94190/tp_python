import unittest


def add(x, y):
    result = (x+y)
    print(result)


class TestAddFunction(unittest.TestCase):
    def test_fonction_add_positive(self):
        x = 5
        y = 10
        result = (x+y)
        self.assertEqual(result, 15)

    def test_fonction_add_negative(self):
        x = -5
        y = -10
        result = (x+y)
        self.assertEqual(result, -15)
