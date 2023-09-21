from django import forms
from register.models import Register

class RegisterForm(forms.ModelForm):
    model = Register
    fields = ['name', 'email', 'address', 'phone', 'password']
    widgests = {'password': forms.PasswordInput()}