from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm): 
    username = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    # help_text uses to make some tip to a field
    email = forms.EmailField(help_text='', widget=forms.EmailInput(attrs={ 'class': 'form-control' }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={ 'class': 'form-control' }))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={ 'class': 'form-control' }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password1')
