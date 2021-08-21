from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from accounts.forms import LoginForm, SingUpForm


class LoginView(View):
    def get(self, request):

        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            login(request, loginForm.user)
            return redirect("/")
        return render(request, 'form.html', {'form': loginForm})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')


class SignUpView(View):

    def get(self, request):
        form = SingUpForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = SingUpForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['re_password']
            User.objects.create_user(**form.cleaned_data)
            return redirect("/")
        return render(request, 'form.html', {'form': form})


