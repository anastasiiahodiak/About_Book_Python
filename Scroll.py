from models.Book import Book


class Scroll(Book):
    A4_LENGTH_IN_METERS = 0.35

    def __init__(self, title, author, publisher, year, genre, length_in_meters):
        super().__init__(title, author, publisher, year, genre)
        self.length_in_meters = length_in_meters

    def get_pages_count(self):
        return self.length_in_meters / self.A4_LENGTH_IN_METERS

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"