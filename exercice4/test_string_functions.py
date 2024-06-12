import unittest
from exercice4.string_functions import reverse_string, is_palindrome


class TestStringFunctions(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("ly"), "yl")
        self.assertEqual(reverse_string("abou"), "uoba")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))


if __name__ == '__main__':
    unittest.main()
