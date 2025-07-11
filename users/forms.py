from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class Userupdateform(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email',]

class Profileupdateform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']