"""
List Books Use Case
Business logic for listing books
"""

from domain.repositories.book_repository import BookRepository
from typing import List
from domain.entities.book import Book

class ListBooksUseCase:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository
    
    def execute(self) -> List[Book]:
        """
        Get all available books
        Returns: List of Book entities
        """
        books = self.book_repository.find_all()
        return books