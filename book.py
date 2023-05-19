"""
Module for implemetation lab1 of Python
"""


class Book:
    """
    Class that represent book with next information...
    """
    __instance = None

    def __init__(self, title="Harry Potter", author="Rowling", publisher="Bloomsbury Children`s",
                 year=2018, genre="fantasy", count_in_warehouse=6):
        """
        Count

        Args:
            title (str): name of book
            author (str): author of book
            publisher (str): publisher of book
            year (int): year of publishing book
            genre (str): genre of book
            count_in_warehouse (int): count of books in warehouse
        """
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.count_in_warehouse = count_in_warehouse

        def get_book(self, quantity):
            """
            Method that return count of books.

            Args:
                quantity (int): count of books

            Returns:
                int: count of books.
            """

            if quantity <= self.count_in_warehouse:
                self.count_in_warehouse -= quantity
            else:
                quantity = self.count_in_warehouse
                self.count_in_warehouse = 0
                return quantity

        def has_more_books(self):
            """
            Method checks whether the specified number of books is in warehouse

            Returns:
                bollen: are books in warehouse
            """
            return self.count_in_warehouse > 0

    @staticmethod
    def get_instance():
        """
        Method returns a static field instance
        Return:

        """
        if not Book.__instance:
            Book.__instance = Book()
        return Book.__instance

    def __str__(self):
        """
        Method returns a string representation of the book

        Returns:
            str: A string representation of the book
        """
        return f"Book(title={self.title}, author={self.author}, publisher={self.publisher}," \
               f" year={self.year}, genre={self.genre}, " \
               f"count in warehouse={self.count_in_warehouse})"

if __name__== '__main__':
    books = [
        Book(),
        Book("Harry Potter", "Rowling", "Bloomsbury Children`s", 2018, "fantasy", 6),
        Book.get_instance(),
        Book.get_instance()
    ]

book1 = Book("Harry Potter", "Rowling", "Bloomsbury Children`s", 2018, "fantasy", 6)
print(book1)

book2 = Book("Harry Potter 2", "Rowling", "Bloomsbury Children`s", 2019, "fantasy", 8)
print(book2)

book3 = Book("Harry Potter 3", "Rowling", "Bloomsbury Children`s", 2020, "fantasy", 9)
print(book3)

book4 = Book("Harry Potter 4", "Rowling", "Bloomsbury Children`s", 2021, "fantasy", 4)
print(book4)