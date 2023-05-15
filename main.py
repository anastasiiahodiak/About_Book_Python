from book import Book

def main():
    books = [Book("Harry Potter", "Rowling", "Bloomsbury Children`s", 2018, "fantasy", 6), Book(), Book.get_instance(), Book.get_instance()]
    for book in books:
        print(book)