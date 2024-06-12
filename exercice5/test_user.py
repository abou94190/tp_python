import unittest
from exercice5.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up a User instance before each test."""
        self.user = User("Abou", 23)

    def test_user_name(self):
        """Test if the user's name is correctly set."""
        self.assertEqual(self.user.name, "Abou")

    def test_user_age(self):
        """Test if the user's age is correctly set."""
        self.assertEqual(self.user.age, 23)


if __name__ == '__main__':
    unittest.main()
