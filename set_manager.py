class SetManager:
    """A class for managing a set of readers from a collection of books."""

    def __init__(self, book_manager):
        """
        Initialize a SetManager object.
        Args:
            book_manager: An instance of BookManager containing the collection of books.
        """
        self.book_manager = book_manager
        self.book_index = 0
        self.reader_index = 0

    def __iter__(self):
        """Return an iterator over the readers of the books in the collection."""
        for book in self.book_manager.books:
            for readers in book.the_best_readers:
                yield readers

    def __len__(self):
        """Return the total number of readers of all the books in the collection."""
        length = 0
        for book in self.book_manager.books:
            length += len(book.the_best_readers)
        return length

    def __getitem__(self, item):
        """
        Get a reader from the set by index.
        Args:
            item: The index of the reader.
        Returns:
            The reader at the specified index.
        Raises:
            IndexError: If the index is out of range.
        """
        for book in self.book_manager.books:
            readers_list = list(book.the_best_readers)
            if item < len(readers_list):
                return readers_list[item]
            item -= len(readers_list)
        raise IndexError("Index out of range")

    def __next__(self):
        """
        Return the next reader from the set.
        Returns:
            The next reader in the set.
        Raises:
            StopIteration: If there are no more readers in the set.
        """
        if self.book_index >= len(self.book_manager.books):
            raise StopIteration

        book = self.book_manager.books[self.book_index]
        readers_list = list(book.the_best_readers)

        if self.reader_index >= len(readers_list):
            self.book_index += 1
            self.reader_index = 0
            return self.__next__()

        value = readers_list[self.reader_index]
        self.reader_index += 1
        return value