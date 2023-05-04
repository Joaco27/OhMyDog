from django.db import models

# Create your models here.
class Perro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField()
    
    def __str__(self):
        return f'Perro: {self.nombre} con {self.edad} años'
    
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    usuario = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    
    
