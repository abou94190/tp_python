import unittest
from exercice6.biblio import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        book1 = "Book 1"
        book2 = "Book 2"
        self.library.add_book(book1)
        self.assertIn(book1, self.library.books)  # Vérifie si le livre 1 a été ajouté
        self.library.add_book(book2)
        self.assertIn(book2, self.library.books)  # Vérifie si le livre 2 a été ajouté

    def test_remove_book(self):
        book = "Book"
        self.library.add_book(book)
        self.assertIn(book, self.library.books)  # Assurez-vous que le livre est dans la bibliothèque avant la suppression
        self.library.remove_book(book)
        self.assertNotIn(book, self.library.books)  # Vérifie si le livre a été supprimé

    def test_remove_nonexistent_book(self):
        book = "Nonexistent Book"
        with self.assertRaises(ValueError):  # Vérifie si une exception ValueError est levée lorsque le livre n'existe pas
            self.library.remove_book(book)


if __name__ == "__main__":
    unittest.main()
