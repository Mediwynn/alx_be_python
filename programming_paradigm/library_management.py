class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_checked_out(self):
        return self._is_checked_out

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', is_checked_out={self._is_checked_out})"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Only instances of Book can be added")

    def get_books(self):
        return self._books

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.check_out():
                return f"'{title}' has been checked out."
        return f"'{title}' is either not available or already checked out."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.return_book():
                return f"'{title}' has been returned."
        return f"'{title}' is either not available or wasn't checked out."

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        return available_books

    def __repr__(self):
        return f"Library(books={self._books})"
