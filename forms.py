from django import forms
from register.models import Register
from register.forms import RegisterForm

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'email', 'address', 'phone', 'password']
        widgests = {'password': forms.PasswordInput()}