from django.contrib import admin
from .models import *

admin.site.register(Perro)
# Register your models here.

admin.site.register(Paseador)
admin.site.register(Cuidador)
admin.site.register(ContactoCuidador)
admin.site.register(ContactoPaseador)
admin.site.register(Turnos)
admin.site.register(PerroAdopcion)
admin.site.register(Cliente)
admin.site.register(ContactoAdop)
admin.site.register(Historial)
admin.site.register(PerroPerdido) 
admin.site.register(Tarjeta)
admin.site.register(Donacion)
