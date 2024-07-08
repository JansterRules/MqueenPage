from django import forms
from .models import Mecanico
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UsuarioForm(ModelForm):
    class Meta:
        model = Mecanico
        fields = "__all__"

# Formulario de registro        
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        label='Correo electrónico', 
        max_length=254, 
        error_messages={'required': 'Este campo es obligatorio.'}
    )

    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput,
        error_messages={'required': 'Este campo es obligatorio.'}
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
        strip=False,
        error_messages={'required': 'Este campo es obligatorio.'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
        }
        error_messages = {
            'username': {
                'unique': "Un usuario con ese nombre ya existe.",
                'required': "Este campo es obligatorio.",
            },
            'email': {
                'unique': "Este correo electrónico ya está en uso.",
                'required': "Este campo es obligatorio.",
                'invalid': "Introduce una dirección de correo válida.",
            },
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(self.Meta.error_messages['username']['unique'])
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(self.Meta.error_messages['email']['unique'])
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
    
# Formulario de ingreso
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=254,
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        strip=False,
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
    )
