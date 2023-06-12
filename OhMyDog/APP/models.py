
from django.db import models


# Aca declaramos todas las tablas de la BD

# Create your models here.
class Perro(models.Model):
    nombre = models.CharField(max_length=15)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField()
    emailDueño = models.EmailField(max_length=30)
    nombreD = models.CharField(max_length=15)
    def __str__(self):
        return f'{self.nombre}'
    
class Cliente(models.Model):
    nombreC = models.CharField(max_length=15)
    usuario = models.CharField(max_length=30)
    contra = models.CharField(max_length=30, null=True)
    mail = models.EmailField(max_length=30)
    telefono = models.IntegerField()
    onLine= models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f'{self.nombreC}'
    

class Paseador(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    zona = models.CharField(max_length=20)
    disponibilidad = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    def __str__(self):
        return f'Paseador: {self.nombre} por {self.zona}'

class ContactoPaseador(models.Model):
    paseador = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    telUsuario = models.IntegerField()
    telPaseador = models.IntegerField()
    def __str__(self):
        return f'El usuario {self.usuario} Tel:{self.telUsuario} quiere contactar a {self.paseador} Tel:{self.telPaseador}'
    
    
class Cuidador(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    zona = models.CharField(max_length=20)
    disponibilidad = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    def __str__(self):
        return f'Cuidador: {self.nombre} por {self.zona}'
    
class ContactoCuidador(models.Model):
    cuidador = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    telUsuario = models.IntegerField()
    telCuidador = models.IntegerField()
    def __str__(self):
        return f'El usuario {self.usuario} Tel:{self.telUsuario} quiere contactar a {self.cuidador} Tel:{self.telCuidador}'
    
class Turnos(models.Model):
    descripcion = models.TextField(max_length=400)
    nombre = models.CharField(max_length=30,null=True,blank=True)#hay que sacarlo
    edad = models.IntegerField(null=True,blank=True)
    raza = models.CharField(max_length=30,null=True,blank=True)
    perro = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    fecha = models.DateField()
    def __str__(self):
        return f'Turno de {self.nombre} de edad {self.edad} raza {self.raza} y descripcion {self.descripcion}'
    
class PerroAdopcion(models.Model):
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    peso= models.IntegerField()
    #edad= models.IntegerField()
    raza= models.CharField(max_length=20)
    descripcion= models.CharField(max_length=30)
    zona= models.CharField(max_length=50)
    castrado = models.CharField(max_length=2)
    def __str__(self):
        return f'se publico el perro {self.nombre}'

class Historial(models.Model):
    nombreP = models.CharField(max_length=30,null=True,blank=True)
    mailD = models.EmailField(max_length=30,null=True,blank=True)
    raza = models.CharField(max_length=30,null=True,blank=True)
    edad = models.IntegerField(null=True,blank=True)
    descripcion = models.CharField(max_length=400)
    motivo  = models.CharField(max_length=30)
    fecha = models.DateField()
    castrado = models.BooleanField(default=False)
    color_pelo  = models.CharField(max_length=30)
    pulsaciones  = models.CharField(max_length=30)
    estudios_complementarios =models.CharField(max_length=400)
    diagnostico_presuntivo = models.CharField(max_length=400)
    tratamiento = models.CharField(max_length=400)
    proxima_visita = models.DateField()