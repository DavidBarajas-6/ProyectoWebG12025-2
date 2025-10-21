from django import forms
from django.forms import inlineformset_factory
from .models import Plan, Menu

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['title', 'content', 'tipo', 'realizado']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'tipo': 'Tipo',
            'realizado': '¿Ya lo hiciste?',
        }
        widgets = {
            'title': forms.TextInput(attrs={'id': 'title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'id': 'content', 'rows': 5, 'class': 'form-control'}),
            'tipo': forms.Select(attrs={'id': 'tipo', 'class': 'form-select'}),
            'realizado': forms.CheckboxInput(attrs={'id': 'realizado', 'class': 'form-check-input'}),
        }

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['comida', 'cantidad']
        labels = {
            'comida': 'Comida',
            'cantidad': 'Cantidad',
        }
        widgets = {
            'comida': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }

MenuFormSet = inlineformset_factory(
    Plan,    Menu,    fields=('comida', 'cantidad'),    extra=1,    can_delete=False
)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

