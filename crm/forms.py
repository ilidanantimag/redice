from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SingUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1' ,'password2',)



