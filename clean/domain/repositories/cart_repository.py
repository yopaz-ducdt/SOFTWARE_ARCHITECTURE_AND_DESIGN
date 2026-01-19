"""
Cart Repository Interface (Abstract)
"""

from abc import ABC, abstractmethod
from domain.entities.cart import Cart, CartItem

class CartRepository(ABC):
    
    @abstractmethod
    def find_by_customer_id(self, customer_id: int) -> Cart:
        """Find cart by customer ID"""
        pass
    
    @abstractmethod
    def get_or_create(self, customer_id: int) -> Cart:
        """Get existing cart or create new one"""
        pass
    
    @abstractmethod
    def add_item(self, cart_id: int, book_id: int, quantity: int) -> CartItem:
        """Add item to cart"""
        pass
    
    @abstractmethod
    def get_items(self, cart_id: int) -> list:
        """Get all items in cart"""
        pass