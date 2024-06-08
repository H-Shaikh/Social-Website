from django import forms


class LoginForm:
    username = forms.CharField
    passsword = forms.CharField(widget=forms.PasswordInput)
    