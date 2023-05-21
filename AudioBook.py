from models.Book import Book


class AudioBook(Book):
    NUMBER_OF_SECONDS_PER_PAGE = 180

    def __init__(self, title, author, publisher, year, genre, time_in_seconds):
        super().__init__(title, author, publisher, year, genre)
        self.time_in_seconds = time_in_seconds

    def get_pages_count(self):
        return self.time_in_seconds / self.NUMBER_OF_SECONDS_PER_PAGE

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"