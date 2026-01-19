"""
Customer Repository Interface (Abstract)
This defines the contract for data access
"""

from abc import ABC, abstractmethod
from domain.entities.customer import Customer

class CustomerRepository(ABC):
    
    @abstractmethod
    def save(self, customer: Customer) -> Customer:
        """Save a customer and return the saved entity"""
        pass
    
    @abstractmethod
    def find_by_id(self, customer_id: int) -> Customer:
        """Find customer by ID"""
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> Customer:
        """Find customer by email"""
        pass
    
    @abstractmethod
    def authenticate(self, email: str, password: str) -> Customer:
        """Authenticate customer with email and password"""
        pass