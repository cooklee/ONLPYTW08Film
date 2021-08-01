from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from accounts.forms import LoginForm


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
