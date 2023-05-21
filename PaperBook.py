from models.Book import Book


class PaperBook(Book):
    BYTES_PER_PAGES_COUNT = 2048

    def __init__(self, title, author, publisher, year, genre, page_count, length_in_mm, height_in_mm):
        super().__init__(title, author, publisher, year, genre)
        self.page_count = page_count
        self.length_in_mm = length_in_mm
        self.height_in_mm = height_in_mm

    def get_pages_count(self):
        return self.page_count

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"