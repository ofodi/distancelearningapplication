from socket import fromshare
from tkinter import Widget
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    username = forms.CharField(initial= '',widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter username..."}))
    email = forms.CharField(initial= '',widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter email address..."}))
    password1 = forms.CharField(initial= '',widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password..."}))
    password2 = forms.CharField(initial= '',widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password..."}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('fname', 'lname', 'gender', 'address', 'contact', 'profile_pic', 'user')
        widgets={
            'fname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}),
            'lname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Address'}),
            'contact':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone no.'}),
            'profile_pic':forms.FileInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'})
        }
        
class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('creg', 'reg_date', 'user')
        widgets = {
            'creg':forms.Select(attrs={'class':'form-control'}),
            'reg_date':forms.DateInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'})
        }