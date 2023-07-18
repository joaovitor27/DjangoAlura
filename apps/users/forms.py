from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de Login', max_length=150, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'João',
        }
    ))
    password = forms.CharField(label='Senha', max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua Senha',
        }
    ))


class RegisterForm(forms.Form):
    username = forms.CharField(label='Nome de Cadastro', max_length=150, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'João',
        }
    ))
    email = forms.EmailField(label='E-mail', max_length=150, required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'joao@silva.com',
        }
    ))
    password1 = forms.CharField(label='Senha', max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua Senha',
        }
    ))
    password2 = forms.CharField(label='Confirme sua Senha', max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua Senha Novamente',
        }
    ))

    def clean_username(self):
        name = self.cleaned_data.get('username')
        if name:
            name = name.strip()
            if " " in name:
                raise forms.ValidationError('Nome de usuário não pode conter espaços!')

        if User.objects.filter(username=name).exists():
            raise forms.ValidationError('Nome de usuário já existe!')

        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.strip()
            if " " in email:
                raise forms.ValidationError('E-mail não pode conter espaços!')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail já existe!')

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas não coincidem!')

        return password2
