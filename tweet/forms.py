from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','image']



class UserRegistration(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')