from django import forms
from .models import Mecanico
from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Mecanico
        fields = "__all__"