from django.db import models
from datetime import datetime as dt
from django.utils import timezone 
# Aca declaramos todas las tablas de la BD

# Create your models here.

class Perro(models.Model):
    nombre = models.CharField(max_length=15)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField(null=True,blank=True)
    peso = models.IntegerField( default=0)
    castrado = models.CharField(max_length=2, default='NO')
    sexo = models.CharField(max_length=15,null=True,blank=True)
    emailDueño = models.EmailField(max_length=30)
    tamaño = models.CharField(max_length=30,null=True)
    fechaNacimiento = models.DateField(default=timezone.now, null=True)
    def __str__(self):
        return f'Perro: {self.nombre} con {self.edad} años, raza {self.raza}, y emailD {self.emailDueño}'
    
class Cliente(models.Model):
    nombreC = models.CharField(max_length=15)
    usuario = models.CharField(max_length=30)
    contra = models.CharField(max_length=30, null=True)
    mail = models.EmailField(max_length=30)
    telefono = models.IntegerField()
    

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
    nombre = models.CharField(max_length=30,null=True,blank=True)
    edad = models.IntegerField(null=True,blank=True)
    raza = models.CharField(max_length=30,null=True,blank=True)
    perro = models.CharField(max_length=100,null=True,blank=True)
    sexo = models.CharField(max_length=15,null=True,blank=True)
    motivo = models.CharField(max_length=100)
    fecha = models.DateField()
    telDueño = models.IntegerField()
    fHoraria = models.CharField(max_length=15,null=True,blank=True)
    estado = models.CharField(max_length=15,null=True,blank=True, default='pendiente')
    motivoRechazo = models.TextField(max_length=400,null=True,blank=True, default='')

      

class PerroAdopcion(models.Model):
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    #edad = models.IntegerField(null=True)
    tamaño = models.CharField(max_length=30,null=True)
    descripcion = models.CharField(max_length=30)
    zona = models.CharField(max_length=50, default='NO')
    estado = models.BooleanField(default=False)
    def __str__(self):
        return f'se publico el perro {self.nombre}'
    
class ContactoAdop(models.Model):
    nombre = models.CharField(max_length=30)
    dueño = models.CharField(max_length=30, default='NO')
    usuario = models.CharField(max_length=30)
    telUsuario = models.IntegerField()
    def __str__(self):
        return f'El usuario {self.usuario} Tel:{self.telUsuario} quiere contactarse por el perro {self.nombre}'
    


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.date}'
    
class PerroPerdido(models.Model):
    usuario = models.CharField(max_length=30)
    dueño = models.CharField(max_length=30)
    telDueño = models.IntegerField()
    nombre = models.CharField(max_length=30)
    raza= models.CharField(max_length=20)
    descripcion= models.CharField(max_length=30)
    zona= models.CharField(max_length=50)
    fechaD= models.DateTimeField()
    imagen = models.ImageField(upload_to='imagenes/',null=True)

   
class ContactoPerdido(models.Model):
    nombreP = models.CharField(max_length=30)
    telDueño = models.IntegerField()
    encontro = models.CharField(max_length=30)
    telEncontro = models.IntegerField()
    def __str__(self):
        if self.nombreP == 'Desconocido':
            return f'{self.encontro} es dueño del perro reportado, contactalo al Telefono:{self.telEncontro}'
        return f'{self.encontro} encontro a {self.nombreP} contactalo al Telefono:{self.telEncontro}'

class Historial(models.Model):
    nombreP = models.CharField(max_length=30,null=True,blank=True)
    mailD = models.EmailField(max_length=30,null=True,blank=True)
    raza = models.CharField(max_length=30,null=True,blank=True)
    edad = models.IntegerField(null=True,blank=True)
    descripcion = models.CharField(max_length=400)
    fecha = models.DateField()
    castrado = models.CharField(max_length=3,null=True,blank=True)
    pulsaciones  = models.CharField(max_length=30)
    estudios_complementarios =models.CharField(max_length=400)
    diagnostico_presuntivo = models.CharField(max_length=400)
    tratamiento = models.CharField(max_length=400)
    proxima_visita = models.DateField(blank=True, null=True)
    
class Donacion(models.Model):
    causa = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=50)
    objetivo = models.IntegerField()
    recaudado = models.IntegerField()
    progreso = models.FloatField()

class Tarjeta(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    mesV = models.IntegerField()
    añoV = models.IntegerField()
    saldo = models.IntegerField()
    codigo = models.IntegerField()
