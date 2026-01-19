"""
Cart and CartItem Entities
"""

class Cart:
    def __init__(self, id=None, customer_id=None, items=None):
        self.id = id
        self.customer_id = customer_id
        self.items = items or []
    
    def add_item(self, book, quantity=1):
        """Add item to cart"""
        item = CartItem(cart_id=self.id, book=book, quantity=quantity)
        self.items.append(item)
        return item
    
    def get_total(self):
        """Calculate total price"""
        return sum(item.get_subtotal() for item in self.items)
    
    def __repr__(self):
        return f"Cart(id={self.id}, customer_id={self.customer_id}, items={len(self.items)})"


class CartItem:
    def __init__(self, id=None, cart_id=None, book=None, quantity=1):
        self.id = id
        self.cart_id = cart_id
        self.book = book
        self.quantity = quantity
    
    def get_subtotal(self):
        """Calculate subtotal for this item"""
        if self.book and self.book.price:
            return self.book.price * self.quantity
        return 0
    
    def __repr__(self):
        return f"CartItem(id={self.id}, book={self.book.title if self.book else None}, qty={self.quantity})"