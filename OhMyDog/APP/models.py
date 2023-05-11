from django.db import models

# Aca declaramos todas las tablas de la BD

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
    

class Paseador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    zona = models.CharField(max_length=20)
    disponibilidad = models.CharField(max_length=30)
    def __str__(self):
        return f'Paseador: {self.nombre} por {self.zona}'

class ContactoPaseador(models.Model):
    paseador = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    telUsuario = models.IntegerField()
    telPaseador = models.IntegerField()
    def __str__(self):
        return f'El usuario {self.usuario} quiere contactar a {self.paseador}'
    
    
class Cuidador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    zona = models.CharField(max_length=20)
    disponibilidad = models.CharField(max_length=30)
    def __str__(self):
        return f'Cuidador: {self.nombre} por {self.zona}'
    
class ContactoCuidador(models.Model):
    cuidador = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    telUsuario = models.IntegerField()
    telCuidador = models.IntegerField()
    def __str__(self):
        return f'El usuario {self.usuario} quiere contactar a {self.cuidador}'
    
class Turnos(models.Model):
    descripcion = models.TextField(max_length=400)
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    raza = models.CharField(max_length=30)
    def __str__(self):
        return f'Turno de {self.nombre} de edad {self.edad} raza {self.raza} y descripcion {self.descripcion}'
    
"""class PerroAdopcion(models.Model):
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    peso= models.IntegerField()
    raza= models.CharField(max_length=20)
    descripcion= models.CharField(max_length=30)
    castrado = models.CharField(max_length=2)
    def __str__(self):
        return f'El usuario {self.usuario} publica al perro {self.nombre}'"""