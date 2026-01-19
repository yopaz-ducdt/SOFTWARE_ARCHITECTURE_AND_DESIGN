"""
Login Customer Use Case
Business logic for customer authentication
"""

from domain.entities.customer import Customer
from domain.repositories.customer_repository import CustomerRepository
from django.contrib.auth.hashers import check_password

class LoginCustomerUseCase:
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository
    
    def execute(self, email: str, password: str) -> Customer:
        """
        Authenticate customer
        Returns: Customer entity if successful
        Raises: ValueError if authentication fails
        """
        if not email or not password:
            raise ValueError("Email and password are required")
        
        # Find customer by email
        customer = self.customer_repository.find_by_email(email)
        
        if not customer:
            raise ValueError("Invalid email or password")
        
        # Check password
        if not check_password(password, customer.password):
            raise ValueError("Invalid email or password")
        
        return customer