"""
Book Repository Interface (Abstract)
"""

from abc import ABC, abstractmethod
from domain.entities.book import Book
from typing import List

class BookRepository(ABC):
    
    @abstractmethod
    def find_all(self) -> List[Book]:
        """Get all books"""
        pass
    
    @abstractmethod
    def find_by_id(self, book_id: int) -> Book:
        """Find book by ID"""
        pass
    
    @abstractmethod
    def save(self, book: Book) -> Book:
        """Save a book"""
        pass