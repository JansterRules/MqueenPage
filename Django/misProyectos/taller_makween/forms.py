from django import forms
from .models import Mecanico
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UsuarioForm(ModelForm):
    class Meta:
        model = Mecanico
        fields = "__all__"



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico', max_length=254)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email
