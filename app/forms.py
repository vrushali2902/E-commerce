from cProfile import label
from msilib.schema import Class
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CustomerRegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

class Meta:
    model = User
    feilds = ['username','email','password1','password2']
    label = {'email':'Email'}
    widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
