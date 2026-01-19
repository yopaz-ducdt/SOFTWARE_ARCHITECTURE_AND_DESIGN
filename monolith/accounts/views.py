from django.shortcuts import render, redirect
from .models import Customer
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                customer = Customer.objects.get(email=email, password=password)
                request.session['customer_id'] = customer.id
                return redirect('book_list')
            except Customer.DoesNotExist:
                error = 'Sai email hoặc mật khẩu'
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form, 'error': error})
