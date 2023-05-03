from .models import *
from django import forms

from django.core.exceptions import ValidationError 

class Perro_form(forms.Form):
    nombre = forms.CharField(max_length=15, required=True, label='Nombre')
    raza = forms.CharField(max_length=15, required=True, label='Raza')
    edad = forms.IntegerField(required=True, label='Edad')

    
    def clean_edad(self):
        data = self.cleaned_data["edad"]
        if data < 1 or data > 20:
            raise ValidationError("Edad invalida")
        return data
