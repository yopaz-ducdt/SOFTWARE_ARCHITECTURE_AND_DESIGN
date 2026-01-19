"""
Register Customer Use Case
Business logic for customer registration
"""

from domain.entities.customer import Customer
from domain.repositories.customer_repository import CustomerRepository
from django.contrib.auth.hashers import make_password

class RegisterCustomerUseCase:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository
    
    def execute(self, name: str, email: str, password: str) -> Customer:
        """
        Register a new customer
        Returns: Customer entity
        Raises: ValueError if validation fails
        """
        # Create customer entity
        customer = Customer(name=name, email=email, password=password)
        
        # Validate
        customer.validate()
        
        # Check if email already exists
        existing = None
        try:
            existing = self.customer_repository.find_by_email(email)
        except:
            pass
        
        if existing:
            raise ValueError("Email already registered")
        
        # Hash password
        customer.password = make_password(password)
        
        # Save to database
        saved_customer = self.customer_repository.save(customer)
        
        return saved_customer