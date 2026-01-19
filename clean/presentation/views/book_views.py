"""
Book Views (Presentation Layer)
"""

from django.shortcuts import render

from application.use_cases.list_books import ListBooksUseCase
from infrastructure.persistence.repositories.django_book_repository import DjangoBookRepository


def book_list(request):
    # Check if user is logged in
    if 'customer_id' not in request.session:
        return redirect('login')
    
    # Use Case
    repo = DjangoBookRepository()
    use_case = ListBooksUseCase(repo)
    
    books = use_case.execute()
    
    return render(request, 'books/book_list.html', {'books': books})