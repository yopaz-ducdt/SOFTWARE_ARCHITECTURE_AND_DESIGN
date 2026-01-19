from django import forms
from .models import Customer

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
