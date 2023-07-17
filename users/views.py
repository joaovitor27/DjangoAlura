from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from users.forms import LoginForm, RegisterForm


# Create your views here.


def login(request: WSGIRequest):
    form_login = LoginForm()
    context = {
        'form_login': form_login
    }
    return render(request, 'users/login.html', context)


def logout(request: WSGIRequest):
    return render(request, 'users/logout.html')


def register(request: WSGIRequest):
    form_register = RegisterForm()
    context = {
        'form_register': form_register
    }
    return render(request, 'users/register.html', context)
