from django.db import models

# Create your models here.
class Perro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField()
    color = models.CharField(max_length=15)
    
    