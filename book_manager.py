class BookManager:
    """
    Class that manages a collection of books.
    """
    def __init__(self):
        """
        Initializes an object of the BookManager class.
        """
        self.books = []

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

    def search_by_year(self, year):
        """
        Performs a search for books by publication year.

        Parameters:
        - year (int): The publication year of the book.

        Returns:
        - A list of books that were published in the specified year.
        """
        return filter(lambda book: book.year == year, self.books)