from models.book import Book


class Scroll(Book):
    """
    Represents a scroll book.
    """

    A4_LENGTH_IN_METERS = 0.35

    def __init__(self, title, author, publisher, year, genre, length_in_meters):
        """
        Initializes a Scroll instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publisher (str): The publisher of the book.
            year (int): The publication year of the book.
            genre (str): The genre of the book.
            length_in_meters (float): The length of the scroll book in meters.
            """
        super().__init__(title, author, publisher, year, genre)
        self.length_in_meters = length_in_meters

    def get_pages_count(self):
        """
        Calculates the number of pages in the scroll book.

        Returns:
            float: The number of pages in the scroll book.
        """
        return self.length_in_meters / self.A4_LENGTH_IN_METERS

    def __str__(self):
        """
        Returns a string representation of the Scroll instance.

        Returns:
            str: The string representation of the Scroll instance.
        """
        return f"{super().__str__()}, " \
               f"length_in_meters={self.length_in_meters}"
