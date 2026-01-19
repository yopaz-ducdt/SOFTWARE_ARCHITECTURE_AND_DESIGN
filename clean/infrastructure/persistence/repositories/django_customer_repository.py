"""
Django Implementation of Customer Repository
"""

from domain.repositories.customer_repository import CustomerRepository
from domain.entities.customer import Customer
from infrastructure.persistence.models import CustomerModel

class DjangoCustomerRepository(CustomerRepository):
    
    def save(self, customer: Customer) -> Customer:
        """Save customer to database"""
        model = CustomerModel(
            name=customer.name,
            email=customer.email,
            password=customer.password
        )
        model.save()
        customer.id = model.id
        return customer
    
    def find_by_id(self, customer_id: int) -> Customer:
        """Find customer by ID"""
        try:
            model = CustomerModel.objects.get(id=customer_id)
            return self._to_entity(model)
        except CustomerModel.DoesNotExist:
            return None
    
    def find_by_email(self, email: str) -> Customer:
        """Find customer by email"""
        try:
            model = CustomerModel.objects.get(email=email)
            return self._to_entity(model)
        except CustomerModel.DoesNotExist:
            return None
    
    def authenticate(self, email: str, password: str) -> Customer:
        """Authenticate customer"""
        try:
            model = CustomerModel.objects.get(email=email, password=password)
            return self._to_entity(model)
        except CustomerModel.DoesNotExist:
            return None
    
    def _to_entity(self, model: CustomerModel) -> Customer:
        """Convert Django model to domain entity"""
        return Customer(
            id=model.id,
            name=model.name,
            email=model.email,
            password=model.password
        )