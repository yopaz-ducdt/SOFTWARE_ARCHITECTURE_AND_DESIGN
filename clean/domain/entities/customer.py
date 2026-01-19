"""
Customer Entity - Core business object
This is independent of any framework or database
"""

class Customer:
    def __init__(self, id=None, name=None, email=None, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    
    def validate(self):
        """Validate customer data"""
        if not self.name or len(self.name) < 2:
            raise ValueError("Name must be at least 2 characters")
        if not self.email or '@' not in self.email:
            raise ValueError("Invalid email address")
        if not self.password or len(self.password) < 6:
            raise ValueError("Password must be at least 6 characters")
        return True
    
    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name}, email={self.email})"