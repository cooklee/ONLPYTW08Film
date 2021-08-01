from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean(self):
        data = super().clean()
        self.user = authenticate(**data)
        if self.user is None:
            raise ValidationError("nie poprawne dane logowania")
        return data


class SingUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Re-password')

    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('re_password'):
            raise ValidationError('Hasła się nie zgadzają!!!')
        return data
