"""
Customer Views (Presentation Layer)
"""

from django.shortcuts import render, redirect
from django import forms

from application.use_cases.register_customer import RegisterCustomerUseCase
from application.use_cases.login_customer import LoginCustomerUseCase
from infrastructure.persistence.repositories.django_customer_repository import DjangoCustomerRepository

# Forms
class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


# Views
def register(request):
    error = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                # Use Case
                repo = DjangoCustomerRepository()
                use_case = RegisterCustomerUseCase(repo)
                
                customer = use_case.execute(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                return redirect('login')
            except ValueError as e:
                error = str(e)
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form, 'error': error})


def login(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                # Use Case
                repo = DjangoCustomerRepository()
                use_case = LoginCustomerUseCase(repo)
                
                customer = use_case.execute(
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                
                # Store customer_id in session
                request.session['customer_id'] = customer.id
                return redirect('book_list')
            except ValueError as e:
                error = str(e)
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form, 'error': error})