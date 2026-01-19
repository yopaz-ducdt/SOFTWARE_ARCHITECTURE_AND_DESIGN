from django.shortcuts import redirect, render
from .models import Cart, CartItem
from books.models import Book
from accounts.models import Customer

def add_to_cart(request, book_id):
    customer = Customer.objects.get(id=request.session["customer_id"])
    cart, _ = Cart.objects.get_or_create(customer=customer)
    book = Book.objects.get(id=book_id)

    CartItem.objects.create(cart=cart, book=book, quantity=1)
    return redirect("view_cart")

def view_cart(request):
    customer = Customer.objects.get(id=request.session["customer_id"])
    cart = Cart.objects.filter(customer=customer).first()
    items = CartItem.objects.filter(cart=cart)
    return render(request, "cart.html", {"items": items})
