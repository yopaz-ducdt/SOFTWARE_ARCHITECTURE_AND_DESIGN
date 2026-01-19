"""
Cart Views (Presentation Layer)
"""

from django.shortcuts import render, redirect

from application.use_cases.add_to_cart import AddToCartUseCase
from application.use_cases.view_cart import ViewCartUseCase
from infrastructure.persistence.repositories.django_cart_repository import DjangoCartRepository
from infrastructure.persistence.repositories.django_book_repository import DjangoBookRepository


def add_to_cart(request, book_id):
    # Check if user is logged in
    if 'customer_id' not in request.session:
        return redirect('login')
    
    customer_id = request.session['customer_id']
    
    try:
        # Use Case
        cart_repo = DjangoCartRepository()
        book_repo = DjangoBookRepository()
        use_case = AddToCartUseCase(cart_repo, book_repo)
        
        use_case.execute(customer_id, book_id, quantity=1)
        return redirect('view_cart')
    except ValueError as e:
        # Handle error
        return redirect('book_list')


def view_cart(request):
    # Check if user is logged in
    if 'customer_id' not in request.session:
        return redirect('login')
    
    customer_id = request.session['customer_id']
    
    # Use Case
    cart_repo = DjangoCartRepository()
    use_case = ViewCartUseCase(cart_repo)
    
    cart = use_case.execute(customer_id)
    
    return render(request, 'cart/cart.html', {'cart': cart})