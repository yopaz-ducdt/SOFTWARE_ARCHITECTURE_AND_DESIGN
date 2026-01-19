"""
Book Entity - Core business object
"""

class Book:
    def __init__(self, id=None, title=None, author=None, price=None, stock=None):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    
    def validate(self):
        """Validate book data"""
        if not self.title:
            raise ValueError("Title is required")
        if not self.author:
            raise ValueError("Author is required")
        if self.price is None or self.price < 0:
            raise ValueError("Price must be non-negative")
        if self.stock is None or self.stock < 0:
            raise ValueError("Stock must be non-negative")
        return True
    
    def is_available(self):
        """Check if book is in stock"""
        return self.stock > 0
    
    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, author={self.author})"