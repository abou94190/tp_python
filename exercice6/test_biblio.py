import unittest
from exercice6.biblio import Book


class TestBook(unittest.TestCase):

    def test_book_initialization(self):
        title = "Nom Livre"
        author = "Autheur du Livre"
        book = Book(title, author)
        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)

    def test_book_str_representation(self):
        title = "Nom Livre"
        author = "Autheur du Livre"
        book = Book(title, author)
        expected_str = f"{title} by {author}"
        self.assertEqual(str(book), expected_str)


if __name__ == '__main__':
    unittest.main()
