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
    
    path('publicaciones', views.publicaciones,name='publicaciones'),
    path('publicar',views.publicar,name='publicar'),
    path('publicarP',views.publicarP,name='publicarP'),
    path('publicarC',views.publicarC,name='publicarC'),
    
    path('turnos',views.turnos,name='turnos'),
    path('publicarAdopcion',views.publicarAdopcion,name='publicarAdopcion'),
    path('registrarCliente',views.registrarCliente,name='registrarCliente'),
    path('LogIn',views.LogIn,name='LogIn'),
    path('LogOut',views.LogOut,name='LogOut'),
    path('listarClientes',views.listarClientes,name='listarClientes'),
    path('borrarCliente/<str:usuario>',views.borrarCliente,name='borrarCliente'),
    path('borrarPerro/<str:emailDueño>/<str:nombre>',views.borrarPerro,name='borrarPerro'),
    path('borrarPerroC/<str:emailDueño>/<str:nombre>',views.borrarPerroC,name='borrarPerroC'),
    path('borrarPerroA/<str:usuario>/<str:nombre>',views.borrarPerroA,name='borrarPerroA'),
    path('listarAdopciones',views.ListarAdopciones,name='ListarAdopciones'),
    path('notificaciones',views.notificaciones,name='notificaciones'),
    path('notiContacto', views.notiContacto,name='notiContacto'),
    path('notiTurnos', views.notiTurnos,name='notiTurnos'),
    path('borrarNotiC/<str:nombreU>/<str:nombreC>/',views.terminarContactoC,name='borrarNotiC'),
    path('borrarNotiP/<str:nombreU>/<str:nombreP>/',views.terminarContactoP,name='borrarNotiP'),
    
    path('registrar',views.registrar,name='registrar'),
    path('registrarPerro',views.registrarPerro,name='registrarPerro'),
    path('losPerros',views.losPerros,name='losPerros'),
    
    path('publicarPerdido', views.publicarPerdido,name='publicarPerdido'),
    path('listarPerdidos', views.listarPerdidos, name='listarPerdidos'),
    path('borrarPerroPerdido/<str:dueño>/<str:nombre>/',views.borrarPerroPerdido, name='borrarPerroPerdido'),
    path('contactarPerd/<str:nombre>/<int:telDueño>/',views.contactarPerd, name='contactarPerd'),
    path('contactarPerdVisit/<str:nombre>/<int:telDueño>/',views.contactarPerdVisit, name='contactarPerdVisit'),
    path('notiPerdidos', views.notiPerdidos, name='notiPerdidos'),
    path('borrarNotiPerd/<str:nombreP>/<str:encontro>/',views.terminarPerd,name='borrarNotiPerd'),
    path('misPerdidos', views.misPerdidos, name='misPerdidos'),
    path('borrarNotificacionT/<str:nombreU>/',views.borrarNotificacionT,name='borrarNotificacionT'),

    path('borrarNotiT/<str:nombre>/',views.borrarNotiT,name='borrarNotiT'),


    path('misPerros',views.misPerros,name='misPerros'),
    path('listarHistorialV',views.listarHistorialV,name='listarHistorialV'),
    path('listarHistorialC',views.listarHistorialC,name='listarHistorialC'),
    path('cargarHistorial',views.cargarHistorial,name='cargarHistorial'),




    path('validate', views.validate, name = 'validate'),
    path('validateC', views.validateC, name = 'validateC'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


