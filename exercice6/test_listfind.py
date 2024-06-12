import unittest


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def list_books(self):
        return [str(book) for book in self.books]

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Book 1", "Author 1")
        self.book2 = Book("Book 2", "Author 2")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_find_book_by_title(self):
        found_book = self.library.find_book_by_title("Book 1")
        self.assertEqual(found_book, self.book1)  # Vérifie si le bon livre est trouvé

    def test_find_nonexistent_book_by_title(self):
        found_book = self.library.find_book_by_title("Nonexistent Book")
        self.assertIsNone(found_book)  # Vérifie si None est retourné lorsque le livre n'existe pas

    def test_list_books(self):
        books = self.library.list_books()
        self.assertIn(str(self.book1), books)  # Vérifie si le livre 1 est dans la liste des livres
        self.assertIn(str(self.book2), books)  # Vérifie si le livre 2 est dans la liste des livres


if __name__ == "__main__":
    unittest.main()
