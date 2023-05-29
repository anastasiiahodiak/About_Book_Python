import logging


def loging_decorator(func):
    """
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.INFO, filename="program_log.log", filemode="w")
        logging.info(f"function call -> {func.__name__} ")
        for i in args:
            logging.info(f"function args -> {i}")
        logging.info(f"function result -> {func(*args, **kwargs)}")
        return func(*args, **kwargs)

    return wrapper

def print_len_of_iterate_object(func):
    """Decorator that prints the length of an iterable object returned by a method."""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if hasattr(result, '__iter__'):
            length = len(result)
        else:
            length = 1
        print("Length of iterate object is : ", length)
        return result

    return wrapper


class BookManager:
    """
    Class that manages a collection of books.
    """
    def __init__(self):
        """
        Initializes an object of the BookManager class.
        """
        self.books = []

    def __len__(self):
        """Return the length of the books collection."""
        return len(self.books)

    def __getitem__(self, item):
        """Get a book from the collection by index."""
        return self.books[item]

    def __iter__(self):
        """Return an iterator for the books collection."""
        return iter(self.books)

    def add_book(self, book):
        """
        Adds a book to the collection.

        Parameters:
            - book (Book): The book object to be added to the collection.
        """
        self.books.append(book)

    def search_by_genre(self, genre):
        """
        Performs a search for books by genre.

        Parameters:
            - genre (str): The genre of the book.

        Returns:
             - A list of books that match the specified genre.
        """
        return filter(lambda book: book.genre == genre, self.books)

    @loging_decorator
    def search_by_year(self, year):
        """
        Performs a search for books by publication year.

        Parameters:
        - year (int): The publication year of the book.

        Returns:
        - A list of books that were published in the specified year.
        """
        return filter(lambda book: book.year == year, self.books)

    def result_of_get_pages_count(self):
        """Return a list of the pages count for each book in the collection."""
        return [book.get_pages_count() for book in self.books]

    def enumerate_objects(self):
        """Enumerate the books in the collection and return a list of index-value pairs."""
        return [
            f"Index => {i} - value => {j}"
            for i, j in enumerate(self.books)
        ]

    def zip_return(self):
        """Return a list of tuples containing a string representation of each book and its pages count."""
        return list(zip(map(lambda x: str(x), self.books), self.result_of_get_pages_count()))

    @print_len_of_iterate_object
    def all_and_any(self, condition):
        """
        Check if all or any of the books in the collection satisfy the given condition.
        Args:
            condition: A function that takes a book as input and returns a boolean value.
        Returns:
            A dictionary with 'all' and 'any' keys, indicating if all or any of the books satisfy the condition.
        """
        any_is_electronic_book = any(condition(book) for book in self.books)
        all_are_electronic_book = all(condition(book) for book in self.books)
        return {"all": all_are_electronic_book, "any": any_is_electronic_book}