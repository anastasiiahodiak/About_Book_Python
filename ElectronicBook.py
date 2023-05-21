from models.Book import Book

class ElectronicBook(Book):
    BYTES_PER_PAGES_COUNT = 2048

    def __init__(self, title, author, publisher, year, genre, format, file_size_in_bytes):
        super().__init__(title, author, publisher, year, genre)
        self.format = format
        self.file_size_in_bytes = file_size_in_bytes

    def get_pages_count(self):
        return self.file_size_in_bytes / self.BYTES_PER_PAGES_COUNT

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"