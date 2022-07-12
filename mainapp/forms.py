from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label = '',widget=forms.TextInput(attrs={'placeholder':'Логин'}))
    password = forms.CharField(label = '',widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})