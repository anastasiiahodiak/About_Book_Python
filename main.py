from managers.BookManager import BookManager
from models.AudioBook import AudioBook
from models.ElectronicBook import ElectronicBook
from models.PaperBook import PaperBook
from models.Scroll import Scroll

book_manager = BookManager()
book_manager.add_book(ElectronicBook("A Thousand Splendid Suns", "Khaled Hosseini", "Riverhead Books", 2007, "historical fiction", "PDF", 1024000))
book_manager.add_book(PaperBook("The Knife of Never Letting Go", "Patrick Ness", "Walker Books Ltd", 2008, "science fiction", 855, 190, 300))
book_manager.add_book(AudioBook("The Hobbit", "J.R.R. Tolkien", "George Allen & Unwin", 1937, "fantasy", 7200))
book_manager.add_book(Scroll("The Power of Positive Thinking", "Norman Vincent Peale", "Prentice Hall Press", 1952, "self-help", 70))
book_manager.add_book(PaperBook("1984", "George Orwell", "Harcourt", 1949, "dystopian fiction", 410, 160, 215))
book_manager.add_book(ElectronicBook("Little Women", "Louisa May Alcott", "Roberts Brothers", 1868, "comedy", "MOBI", 512000))

for book in book_manager.books:
    print(book)

print("\n")

books_by_genre = book_manager.search_by_genre("fantasy")
print("Books by genre:")
for book in books_by_genre:
    print(book)

print("\n")

books_by_year = book_manager.search_by_year(2007)
print("Books by year:")
for book in books_by_year:
    print(book)