from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from apps.users.forms import LoginForm, RegisterForm


# Create your views here.


def login(request: WSGIRequest):
    form_login = LoginForm()
    if request.method == 'POST':
        form_login = LoginForm(request.POST)
        if form_login.is_valid():
            name = form_login['username'].value()
            password = form_login['password'].value()

            user = auth.authenticate(request, username=name, password=password)

            if not user:
                messages.error(request, 'Usuário ou senha incorretos!')
                return redirect('login')

            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index')

    context = {
        'form_login': form_login
    }
    return render(request, 'users/login.html', context)


def logout(request: WSGIRequest):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')


def register(request: WSGIRequest):

    form_register = RegisterForm()

    if request.method == 'POST':
        form_register = RegisterForm(request.POST)
        if form_register.is_valid():
            name = form_register['username'].value()
            email = form_register['email'].value()
            password = form_register['password1'].value()

            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')

    context = {
        'form_register': form_register
    }
    return render(request, 'users/register.html', context)
