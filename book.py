class Book:
    instance = None

    def __init__(self, title="Harry Potter", author="Rowling", publisher="Bloomsbury Children`s", year=2018,
                 genre="fantasy", count_in_warehouse=6):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._year = year
        self._genre = genre
        self._count_in_warehouse = count_in_warehouse

        def get_book(self, quantity):
            if quantity <= self._count_in_warehouse:
                self._count_in_warehouse -= quantity
                return quantity
            else:
                quantity = self._count_in_warehouse
                self._count_in_warehouse = 0
                return quantity

        def has_more_books(self):
            return self._count_in_warehouse > 0

    @staticmethod
    def get_instance():
        if not Book.instance:
            Book.instance = Book()
        return Book.instance

    def __str__(self):
        return f"Book(title={self._title}, author={self._author}, publisher={self._publisher}," \
               f" year={self._year}, genre={self._genre}, count in warehouse={self._count_in_warehouse})"