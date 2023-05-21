class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_genre(self, genre):
        return [book for book in self.books if book.genre == genre]

    def search_by_year(self, year):
        return [book for book in self.books if book.year == year]