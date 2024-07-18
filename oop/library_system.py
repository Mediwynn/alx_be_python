class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library():
    def __init__(self) -> None:
        pass

    def add_book(self, books):
        book_list.append(books)

    def list_books(self, book_list):
        if book_list == "classic_book":
            print(f"Book: {self.title} by {self.author}")
        elif book_list == "digital_novel":
            print(f"EBook: {self.title} by {self.author}, {self.file_size}")
        elif book_list == "paper_novel":
            print(f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}")
        else:
            print("Error, invalid input")

book_list = []