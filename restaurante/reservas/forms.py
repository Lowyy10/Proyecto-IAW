# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Perfil, Valoracion


class PerfilForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label='Nombre de Usuario')  # Mantén el campo aquí

    class Meta:
        model = Perfil
        fields = ['bio', 'tel']  # No incluyas 'username' aquí

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username

    def save(self, commit=True):
        perfil = super(PerfilForm, self).save(commit=False)
        perfil.user.username = self.cleaned_data['username']
        if commit:
            perfil.user.save()
            perfil.save()
        return perfil


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Usuario',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Introduce tu usuario'})  # Texto en el campo
    )

    class Meta:
        model = User
        fields = ('username', 'email' , 'password1', 'password2')  # Añade otros campos que desees
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Introduce tu contraseña'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña'}),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={'placeholder': 'Introduce tu usuario'})  # Texto en el campo
    )

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Introduce tu contraseña'}),
        }
from django import forms
from .models import MisPedidos

class MisPedidosForm(forms.ModelForm):
    class Meta:
        model = MisPedidos
        fields = ['nombre_persona', 'plato', 'cantidad', 'observaciones']
        widgets = {
            'nombre_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'plato': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
        }

#Valoraciones

class ValoracionForm(forms.ModelForm):
    class Meta:
        model = Valoracion
        fields = ['valoracion']  # Solo necesitas el campo de valoración

    def __init__(self, *args, **kwargs):
        super(ValoracionForm, self).__init__(*args, **kwargs)
        self.fields['valoracion'].widget.attrs.update({'class': 'valoracion-select'})
