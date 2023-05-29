from models.book import Book


class PaperBook(Book):
    """
    Represents a paper book.
    """
    def __init__(self, title, author, publisher, year, genre, page_count, length_in_mm, height_in_mm):
        """
        Initializes a PaperBook instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publisher (str): The publisher of the book.
            year (int): The publication year of the book.
            genre (str): The genre of the book.
            page_count (int): The number of pages in the paper book.
            length_in_mm (float): The length of the book in millimeters.
            height_in_mm (float): The height of the book in millimeters.
        """
        super().__init__(title, author, publisher, year, genre)
        self.page_count = page_count
        self.length_in_mm = length_in_mm
        self.height_in_mm = height_in_mm

    def get_pages_count(self):
        """
        Returns the number of pages in the paper book.

        Returns:
            int: The number of pages in the paper book.
        """
        return self.page_count

    def __str__(self):
        """
        Returns a string representation of the PaperBook instance.

        Returns:
            str: The string representation of the PaperBook instance.
        """
        return f"{super().__str__()}, " \
               f"page_count={self.page_count}, " \
               f"length_in_mm={self.length_in_mm}, " \
               f"height_in_mm={self.height_in_mm}"