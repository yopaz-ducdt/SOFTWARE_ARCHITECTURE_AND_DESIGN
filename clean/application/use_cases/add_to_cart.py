"""
Add to Cart Use Case
Business logic for adding items to cart
"""

from domain.repositories.cart_repository import CartRepository
from domain.repositories.book_repository import BookRepository
from domain.entities.cart import CartItem

class AddToCartUseCase:
    def __init__(self, cart_repository: CartRepository, book_repository: BookRepository):
        self.cart_repository = cart_repository
        self.book_repository = book_repository
    
    def execute(self, customer_id: int, book_id: int, quantity: int = 1) -> CartItem:
        """
        Add book to customer's cart
        Returns: CartItem entity
        Raises: ValueError if book not found or out of stock
        """
        # Validate
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        # Check if book exists
        book = self.book_repository.find_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        
        # Check stock
        if not book.is_available():
            raise ValueError("Book is out of stock")
        
        # Get or create cart
        cart = self.cart_repository.get_or_create(customer_id)
        
        # Add item to cart
        cart_item = self.cart_repository.add_item(cart.id, book_id, quantity)
        
        return cart_item