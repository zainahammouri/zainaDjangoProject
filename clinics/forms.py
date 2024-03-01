from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .views import * 

class UserRigister(UserCreationForm):
    first_name = forms.CharField(max_length=30 , help_text='Required. 30')
    last_name = forms.CharField(max_length=30 , help_text='Required. 30')
    email= forms.EmailField(max_length=250, help_text='Required. 250')
    phone= forms.CharField(max_length=10 , help_text='Required. 10')
    date= forms.DateField()
    city= forms.CharField(max_length=50, help_text='Required. 50')
    password= forms.CharField(widget=forms.PasswordInput ,help_text='Required. 8')

    class Meta:
        model=User
        fields=('first_name', 'last_name', 'email','phone','date','city', 'password')


class contactus(UserCreationForm):
    name=forms.CharField(max_length=100 ,help_text='Required. 100')
    email=forms.EmailField(max_length=250 , help_text='Required. 250')
    message=forms.CharField(max_length=1000 ,help_text='Required. 1000 ')

    class Meta:
        model=User
        fields=('name', 'email', 'message')


class login(UserCreationForm):
    phone=forms.CharField(max_length=10 ,help_text='Required. 10')
    password=forms.CharField(max_length=8 ,help_text='Required. 8')

    class Meta:
        model=User
        fields=('phone', 'password')

