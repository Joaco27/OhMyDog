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
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


