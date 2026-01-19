"""
View Cart Use Case
Business logic for viewing cart
"""

from domain.repositories.cart_repository import CartRepository
from domain.entities.cart import Cart

class ViewCartUseCase:
    def __init__(self, cart_repository: CartRepository):
        self.cart_repository = cart_repository
    
    def execute(self, customer_id: int) -> Cart:
        """
        Get customer's cart with all items
        Returns: Cart entity with items
        """
        cart = self.cart_repository.find_by_customer_id(customer_id)
        return cart