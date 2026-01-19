"""
Django Implementation of Book Repository
"""

from domain.repositories.book_repository import BookRepository
from domain.entities.book import Book
from infrastructure.persistence.models import BookModel
from typing import List

class DjangoBookRepository(BookRepository):
    
    def find_all(self) -> List[Book]:
        """Get all books"""
        models = BookModel.objects.all()
        return [self._to_entity(model) for model in models]
    
    def find_by_id(self, book_id: int) -> Book:
        """Find book by ID"""
        try:
            model = BookModel.objects.get(id=book_id)
            return self._to_entity(model)
        except BookModel.DoesNotExist:
            return None
    
    def save(self, book: Book) -> Book:
        """Save book to database"""
        model = BookModel(
            title=book.title,
            author=book.author,
            price=book.price,
            stock=book.stock
        )
        model.save()
        book.id = model.id
        return book
    
    def _to_entity(self, model: BookModel) -> Book:
        """Convert Django model to domain entity"""
        return Book(
            id=model.id,
            title=model.title,
            author=model.author,
            price=float(model.price),
            stock=model.stock
        )