"""
Django Implementation of Cart Repository
"""

from domain.repositories.cart_repository import CartRepository
from domain.entities.cart import Cart, CartItem
from infrastructure.persistence.models import CartModel, CartItemModel, CustomerModel, BookModel
from infrastructure.persistence.repositories.django_book_repository import DjangoBookRepository

class DjangoCartRepository(CartRepository):
    
    def __init__(self):
        self.book_repo = DjangoBookRepository()
    
    def find_by_customer_id(self, customer_id: int) -> Cart:
        """Find cart by customer ID"""
        try:
            cart_model = CartModel.objects.get(customer_id=customer_id)
            return self._to_entity(cart_model)
        except CartModel.DoesNotExist:
            return Cart(customer_id=customer_id, items=[])
    
    def get_or_create(self, customer_id: int) -> Cart:
        """Get existing cart or create new one"""
        try:
            customer = CustomerModel.objects.get(id=customer_id)
        except CustomerModel.DoesNotExist:
            raise ValueError("Customer not found")
        
        cart_model, created = CartModel.objects.get_or_create(customer=customer)
        return self._to_entity(cart_model)
    
    def add_item(self, cart_id: int, book_id: int, quantity: int) -> CartItem:
        """Add item to cart"""
        cart_model = CartModel.objects.get(id=cart_id)
        book_model = BookModel.objects.get(id=book_id)
        
        item_model = CartItemModel.objects.create(
            cart=cart_model,
            book=book_model,
            quantity=quantity
        )
        
        book = self.book_repo.find_by_id(book_id)
        return CartItem(
            id=item_model.id,
            cart_id=cart_id,
            book=book,
            quantity=quantity
        )
    
    def get_items(self, cart_id: int) -> list:
        """Get all items in cart"""
        item_models = CartItemModel.objects.filter(cart_id=cart_id).select_related('book')
        items = []
        for item_model in item_models:
            book = self.book_repo._to_entity(item_model.book)
            item = CartItem(
                id=item_model.id,
                cart_id=cart_id,
                book=book,
                quantity=item_model.quantity
            )
            items.append(item)
        return items
    
    def _to_entity(self, model: CartModel) -> Cart:
        """Convert Django model to domain entity"""
        items = self.get_items(model.id)
        return Cart(
            id=model.id,
            customer_id=model.customer_id,
            items=items
        )