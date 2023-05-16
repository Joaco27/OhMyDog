from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

#Declarar rutas para hacer cuando se ingresan direcciones e invocar funciones de views

urlpatterns = [
    path('',views.index,name='index'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('listarAlgo',views.listarAlgo,name='listarAlgo'),
    path('formulario',views.agregarAlgo,name='formulario'),
    path('paseadores',views.listarPaseadores,name='paseadores'),
    path('cuidadores',views.listarCuidadores,name='cuidadores'),
    path('contactarC/<str:nombre>/<int:telefono>/',views.contactarC,name='contactarC'),
    path('contactarP/<str:nombre>/<int:telefono>/',views.contactarP,name='contactarP'),
    path('publicar',views.publicar,name='publicar'),
    path('publicarP',views.publicarP,name='publicarP'),
    path('publicarC',views.publicarC,name='publicarC'),
    path('turnos',views.turnos,name='turnos'),
    path('publicarAdopcion',views.publicarAdopcion,name='publicarAdopcion'),
    path('registrarCliente',views.registrarCliente,name='registrarCliente'),
    path('LogIn',views.LogIn,name='LogIn'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


