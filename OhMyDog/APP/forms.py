from .models import *
from django import forms

from django.core.exceptions import ValidationError 

# Aca creamos los formularios

class Perro_form(forms.ModelForm):
    # Meta sirve para enlazar con la BD
    class Meta:
        model = Perro
        fields = ['nombre','raza', 'edad']
    # Creamos los campos del formulario
    nombre = forms.CharField(max_length=15, required=True, label='Nombre')
    raza = forms.CharField(max_length=15, required=True, label='Raza')
    edad = forms.IntegerField(required=True, label='Edad')

    # Clean son validaciones 
    def clean_edad(self):
        data = self.cleaned_data["edad"]
        if data < 1 or data > 20:
            raise ValidationError("Edad invalida")
        return data
    
class Paseador_form(forms.ModelForm):
    class Meta:
        model=Paseador
        fields=['nombre', 'telefono', 'zona', 'disponibilidad']
    nombre = forms.CharField(max_length=50, required=True, label='Nombre')
    telefono = forms.IntegerField(required=True, label='Telefono')
    zona = forms.CharField(max_length=20, required=True, label='Zona')
    disponibilidad = forms.CharField(max_length=30, required=True, label='Disponibilidad')
    
    def clean_telefono(self):
        data=self.cleaned_data["telefono"]
        if len(str(data)) < 7:
            raise ValidationError("Telefono invalido")
        return data
    
class Cuidador_form(forms.ModelForm):
    class Meta:
        model=Cuidador
        fields=['nombre', 'telefono', 'zona', 'disponibilidad']
    nombre = forms.CharField(max_length=50, required=True, label='Nombre')
    telefono = forms.IntegerField(required=True, label='Telefono')
    zona = forms.CharField(max_length=20, required=True, label='Zona')
    disponibilidad = forms.CharField(max_length=30, required=True, label='Disponibilidad')
    
    def clean_telefono(self):
        data=self.cleaned_data["telefono"]
        if len(str(data)) < 7:
            raise ValidationError("Telefono invalido")
        return data
class Turnos_form(forms.ModelForm):
    # Meta sirve para enlazar con la BD
    class Meta:
        model = Turnos
        fields = ['descripcion','raza', 'edad','nombre']
    # Creamos los campos del formulario
    descripcion = forms.CharField(max_length=400, required=True, label='Descripcion')
    nombre = forms.CharField(max_length=15, required=True, label='Nombre')
    raza = forms.CharField(max_length=15, required=True, label='Raza')
    edad = forms.IntegerField(required=True, label='Edad')

    # Clean son validaciones 
    def clean_edad(self):
        data = self.cleaned_data["edad"]
        if data < 1 or data > 20:
            raise ValidationError("Edad invalida")
        return data