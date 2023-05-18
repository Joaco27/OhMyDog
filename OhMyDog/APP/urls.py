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
    path('contactarCVisit/<str:nombre>/<int:telefono>/',views.contactarCVisit,name='contactarCVisit'),
    path('borrarC/<int:telefono>/',views.borrarC,name='borrarC'),
    
    path('contactarP/<str:nombre>/<int:telefono>/',views.contactarP,name='contactarP'),
    path('contactarPVisit/<str:nombre>/<int:telefono>/',views.contactarPVisit,name='contactarPVisit'),
    path('borrarP/<int:telefono>/',views.borrarP,name='borrarP'),
    
    path('publicar',views.publicar,name='publicar'),
    path('publicarP',views.publicarP,name='publicarP'),
    path('publicarC',views.publicarC,name='publicarC'),
    
    path('turnos',views.turnos,name='turnos'),
    path('publicarAdopcion',views.publicarAdopcion,name='publicarAdopcion'),
    path('registrarCliente',views.registrarCliente,name='registrarCliente'),
    path('LogIn',views.LogIn,name='LogIn'),
    path('LogOut',views.LogOut,name='LogOut'),
    path('ListarAdopciones',views.ListarAdopciones,name='ListarAdopciones'),
    path('misPerros',views.misPerros,name='misPerros'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


