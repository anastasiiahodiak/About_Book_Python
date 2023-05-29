from models.book import Book


class AudioBook(Book):
    """
    Represents an audiobook.
    """

    NUMBER_OF_SECONDS_PER_PAGE = 180

    def __init__(self, title, author, publisher, year, genre, time_in_seconds):
        """
        Initializes an AudioBook instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publisher (str): The publisher of the book.
            year (int): The publication year of the book.
            genre (str): The genre of the book.
            time_in_seconds (int): The duration of the audiobook in seconds.
        """
        super().__init__(title, author, publisher, year, genre)
        self.time_in_seconds = time_in_seconds

    def get_pages_count(self):
        """
        Calculates the number of pages in the audiobook.

        Returns:
            float: The number of pages in the audiobook.
        """
        return self.time_in_seconds / self.NUMBER_OF_SECONDS_PER_PAGE

    def __str__(self):
        """
        Returns a string representation of the AudioBook instance.

        Returns:
            str: The string representation of the AudioBook instance.
        """
        return f"{super().__str__()}, " \
               f"time_in_seconds={self.time_in_seconds}"