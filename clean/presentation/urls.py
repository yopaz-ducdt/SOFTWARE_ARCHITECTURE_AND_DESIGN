"""
URL Configuration for Presentation Layer
"""

from django.urls import path
from presentation.views import customer_views, book_views, cart_views

urlpatterns = [
    # Customer URLs
    path('accounts/register/', customer_views.register, name='register'),
    path('accounts/login/', customer_views.login, name='login'),
    
    # Book URLs
    path('books/', book_views.book_list, name='book_list'),
    
    # Cart URLs
    path('cart/', cart_views.view_cart, name='view_cart'),
    path('cart/add/<int:book_id>/', cart_views.add_to_cart, name='add_to_cart'),
]