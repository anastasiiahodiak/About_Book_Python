"""
Module for implemetation lab1 of Python
"""
from abc import ABC, abstractmethod


class Book(ABC):
    """
    Class that represent book with next information...
    """

    def __init__(self, title="Harry Potter", author="Rowling", publisher="Bloomsbury Children`s",
                 year=2018, genre="fantasy"):
        """
        Count

        Args:
            title (str): name of book
            author (str): author of book
            publisher (str): publisher of book
            year (int): year of publishing book
            genre (str): genre of book
        """
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self._the_best_readers = set()

    def __iter__(self):
        return iter(self._the_best_readers)

    @abstractmethod
    def get_pages_count(self):
        pass


    def __str__(self):
        """
        Method returns a string representation of the book

        Returns:
            str: A string representation of the book
        """
        return f"Book(title={self.title}, author={self.author}, publisher={self.publisher}," \
               f" year={self.year}, genre={self.genre})"