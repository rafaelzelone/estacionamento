from .models import Carro
from django import forms

class EntradaCarros(forms.ModelForm):
     class Meta:
        model = Carro
        fields = [
            'placa',
            'slug' ,
            'modelo',
            'marca', 
            'proprietario',
            'hora',
            'minutos',
        ]