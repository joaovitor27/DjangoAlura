from django import forms


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