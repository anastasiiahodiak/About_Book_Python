from models.book import Book


class ElectronicBook(Book):
    """
    Represents an electronic book.
    """

    BYTES_PER_PAGES_COUNT = 2048

    def __init__(self, title, author, publisher, year, genre, format, file_size_in_bytes):
        """
        Initializes an ElectronicBook instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publisher (str): The publisher of the book.
            year (int): The publication year of the book.
            genre (str): The genre of the book.
            format (str): The format of the electronic book.
            file_size_in_bytes (int): The size of the book file in bytes.
        """

        super().__init__(title, author, publisher, year, genre)
        self.format = format
        self.file_size_in_bytes = file_size_in_bytes

    def get_pages_count(self):
        """
        Calculates the number of pages in the book.

        Returns:
            float: The number of pages in the book.
        """
        return self.file_size_in_bytes / self.BYTES_PER_PAGES_COUNT

    def __str__(self):
        return f"{super().__str__()}, " \
               f"format={self.format}, " \
               f"file_size_in_bytes={self.file_size_in_bytes}"