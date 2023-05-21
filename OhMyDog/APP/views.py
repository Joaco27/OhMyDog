from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse
from itertools import chain

#Declarar funciones para hacer cuando se ingresan direcciones

# Create your views here.
usuario = {
    "nombre": "",
    "esCliente": False,
    "esVeterinario": False,
}
def getUsuario():
    return usuario

def index(request):
    context ={
        'usuario':usuario
    }
    return render(request, 'paginas/index.html', context)

def registrarCliente(request):
    if request.method == 'POST':
        form = Cliente_form(request.POST) 
        if form.is_valid(): 
            
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente registrado con exito', extra_tags="tag1")

            return redirect("index")
    else:
        form = Cliente_form()
        
    context = {
        'form': form,
        'usuario':usuario,
    }
    return render(request, 'paginas/registrarCliente.html', context)

def registrarPerro(request):
    if request.method == 'POST':
        form = Perro_form(request.POST) 
        if form.is_valid(): 
            
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Perro registrado con exito', extra_tags="tag1")

            return redirect("index")
    else:
        form = Perro_form()
        
    context = {
        'form': form,
        'usuario':usuario
    }
    return render(request, 'paginas/registrarPerro.html', context)

def borrarPerro(request, emailDueño, nombre):
    perro = Perro.objects.get(emailDueño=emailDueño, nombre=nombre)
    perro.delete()
    messages.add_message(request, messages.SUCCESS, 'Perro Eliminado', extra_tags="tag1")
    
    return redirect("losPerros")

def borrarPerroA(request,usuario, nombre):
    perro = PerroAdopcion.objects.get(usuario=usuario, nombre=nombre)
    perro.delete()
    messages.add_message(request, messages.SUCCESS, 'la publicación se elimino con éxito', extra_tags="tag1")

    return redirect("ListarAdopciones")



def borrarPerroC(request, emailDueño, nombre):
    perro = Perro.objects.get(emailDueño=emailDueño, nombre=nombre)
    perro.delete()
    messages.add_message(request, messages.SUCCESS, 'Perro Eliminado', extra_tags="tag1")
    
    return redirect("misPerros")

def LogIn(request):
    if request.method == 'POST':
        form = LogIn_form(request.POST) 
        if form.is_valid(): 
            usuario["nombre"] = form.cleaned_data["usuario"]
            usuario['esCliente'] = True
            if usuario['nombre'] == "Veterinario":
                usuario['esVeterinario'] = True
                usuario['esCliente'] = False
            messages.add_message(request, messages.SUCCESS, 'Iniciaste Sesion', extra_tags="tag1")

            return redirect("index")
    else:
        form = LogIn_form()
        
    context = {
        'form': form,
        'usurio':usuario,
    }
    return render(request, 'paginas/LogIn.html', context)

def LogOut(request):
    usuario["nombre"] = ""
    usuario["contra"] = ""
    usuario['esCliente'] = False
    usuario['esVeterinario'] = False
    
    messages.add_message(request, messages.SUCCESS, 'Cerraste Sesion', extra_tags="tag1")
    
    return redirect("index")

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def listarAlgo(request):
    context = Perro.objects.all()
    #context = Perro.objects.filter(nombre__icontains='Papeto')
    #context = Perro.objects.filter(edad__gt=5)
    return render(request, 'paginas/listarAlgo.html', {'context': context})

def agregarAlgo(request):
    #form = Perro_form(request.POST, request.FILES or None)
    if request.method == 'POST':
        form = Perro_form(request.POST) #Guardo formulario
        if form.is_valid(): #Si pasa todos los clean
            
            form.save()  #Subir a la BD
            messages.add_message(request, messages.SUCCESS, 'Consulta enviada con exito', extra_tags="tag1")

            return redirect("index")
    else:
        form = Perro_form()
        
    context = {
        'form': form,
    }
    return render(request, 'paginas/formulario.html', context)

def listarCuidadores(request):
    cuid = Cuidador.objects.all()
    context = {'context': cuid,
               'usuario': usuario}
    return render(request, 'paginas/listaCuidadores.html', context)
    
def listarPaseadores(request): 
    pasea = Paseador.objects.all()
    context = {'context': pasea,
               'usuario': usuario}
    return render(request, 'paginas/listaPaseadores.html', context)

def ListarAdopciones(request): 
    adop = PerroAdopcion.objects.all()
    context = {'context': adop,
               'usuario': usuario}
    return render(request, 'paginas/ListarAdopciones.html', context)

def misPerros(request): 
    usu = Cliente.objects.filter(usuario=usuario["nombre"]).first()
    lista = Perro.objects.filter(emailDueño=usu.mail)
    context = {'context': lista,
               'usuario': usuario}
    return render(request, 'paginas/misPerros.html', context)

def losPerros(request): 
    lista = Perro.objects.all()
    context = {'context': lista,
               'usuario': usuario}
    return render(request, 'paginas/losPerros.html', context)

def contactarC(request, nombre, telefono):
    cli =  Cliente.objects.get(usuario=usuario["nombre"])
    cuida = ContactoCuidador(
        cuidador =  nombre,
        telCuidador = telefono,
        usuario = cli.nombreC,
        telUsuario = cli.telefono,
    )
    cuida.save()
    messages.add_message(request, messages.SUCCESS, 'Pronto se pondran en contacto con usted', extra_tags="tag1")
    return redirect("index")

def contactarCVisit(request, nombre, telefono):
    if request.method == 'POST':
        form = contacto_form(request.POST) 
        if form.is_valid():
            contactoNuevo = ContactoCuidador(
                cuidador = nombre,
                telCuidador = telefono,
                usuario = form.cleaned_data.get('usuario'),
                telUsuario = form.cleaned_data.get('telefono')
            )
            contactoNuevo.save()
            messages.add_message(request, messages.SUCCESS, 'Pronto se pondran en contacto con usted', extra_tags="tag1")

            return redirect("index")
    else:
        form = contacto_form()
    #url_params = reverse('contactarCVisit',args=[nombre,telefono])
    context = {
        'form': form,
        'usuario':usuario,
        'nombre' : nombre,
        'telefono' : telefono,    
        }
    return render(request, 'paginas/contactarCVisitante.html', context)

def contactarP(request, nombre, telefono):
    cli =  Cliente.objects.get(usuario=usuario["nombre"])
    pasea = ContactoPaseador(
        paseador =  nombre,
        telPaseador = telefono,
        usuario = cli.nombreC,
        telUsuario = cli.telefono,
    )
    pasea.save()
    messages.add_message(request, messages.SUCCESS, 'Pronto se pondran en contacto con usted', extra_tags="tag1")
    return redirect("index")

def contactarPVisit(request, nombre, telefono):
    if request.method == 'POST':
        form = contacto_form(request.POST) 
        if form.is_valid():
            contactoNuevo = ContactoPaseador(
                paseador = nombre,
                telPaseador = telefono,
                usuario = form.cleaned_data.get('usuario'),
                telUsuario = form.cleaned_data.get('telefono')
            )
            contactoNuevo.save()
            messages.add_message(request, messages.SUCCESS, 'Pronto se pondran en contacto con usted', extra_tags="tag1")

            return redirect("index")
    else:
        form = contacto_form()
        
    #url_params = reverse('contactarPVisit',args=[nombre,telefono])
    context = {
        'form': form,
        'usuario':usuario,
        'nombre' : nombre,
        'telefono' : telefono,
    }
    return render(request, 'paginas/contactarPVisitante.html', context)

def publicar(request):
    context ={
        'usuario':usuario
    }
    return render(request,'paginas/publicar.html', context)

def registrar(request):
    context ={
        'usuario':usuario
    }
    return render(request,'paginas/registrar.html', context)

def publicarC(request):
    if request.method == 'POST':
        form = Cuidador_form(request.POST) #Guardo formulario
        if form.is_valid(): #Si pasa todos los clean
            
            form.save()  #Subir a la BD
            messages.add_message(request, messages.SUCCESS, 'Cuidador publicado con exito', extra_tags="tag1")

            return redirect("index")
    else:
        form = Cuidador_form()
        
    context = {
        'form': form,
        'usuario': usuario,
    }
    return render(request, 'paginas/agregarCuidador.html', context)

def borrarC(request, telefono):
    cuidador = Cuidador.objects.get(telefono=telefono)
    cuidador.delete()
    messages.add_message(request, messages.SUCCESS, 'Cuidador Eliminado', extra_tags="tag1")
    return redirect("cuidadores")

def publicarP(request):
    if request.method == 'POST':
        form = Paseador_form(request.POST)
        if form.is_valid():
            
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'Paseador publicado con exito', extra_tags="tag1")

            return redirect("index")
    else:
        form = Paseador_form()
        
    context = {
        'form': form,
        'usuario': usuario,
    }
    return render(request, 'paginas/agregarPaseador.html', context)

def borrarP(request, telefono):
    paseador = Paseador.objects.get(telefono=telefono)
    paseador.delete()
    messages.add_message(request, messages.SUCCESS, 'Paseador Eliminado', extra_tags="tag1")
    
    return redirect("paseadores")

def turnos(request):
    if request.method == 'POST':
        form = Turnos_form(request.POST)
        if form.is_valid():
            
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'El veterinario se pondra en contacto pronto', extra_tags="tag1")

            return redirect("index")
    else:
        form = Turnos_form()
    
    context = {
        'form': form,
        'usuario' : usuario,
    }
    return render(request, 'paginas/turnos.html', context)


def publicarAdopcion(request):
    if request.method == 'POST':
        form = perroAdopcion_form(request.POST)
        if form.is_valid():
            
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'Se ha publicado perro en adopcion', extra_tags="tag1")

            return redirect("index")
    else:
        form = perroAdopcion_form()
    
    context = {
        'form': form,
        'usuario' : usuario,
    }
    return render(request, 'paginas/publicarAdopcion.html', context)

def listarClientes(request):
    cli = Cliente.objects.all()
    context = {
        'context':cli,
        'usuario':usuario
    }
    return render(request, 'paginas/listarClientes.html', context)

def borrarCliente(request, usuario):
    cli = Cliente.objects.get(usuario=usuario)
    cli.delete()
    messages.add_message(request, messages.SUCCESS, 'Cliente Eliminado', extra_tags="tag1")
    
    return redirect("listarClientes")

def notificaciones(request):
    context ={
        'usuario':usuario
    }
    return render(request,'paginas/notificaciones.html', context)
    
def notiContacto(request):
    datosC = ContactoCuidador.objects.all()
    datosP = ContactoPaseador.objects.all()
    #d = chain(datosC,datosP)
    context ={
        'usuario':usuario,
        'paseadores':datosP,
        'cuidadores':datosC,
    }
    return render(request,'paginas/notiContactos.html', context)

def terminarContactoC(request, nombreU, nombreC):
    
    ContactoCuidador.objects.filter(usuario=nombreU,cuidador=nombreC).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Consulta efectuada', extra_tags="tag1")

    return redirect("notiContacto")

def terminarContactoP(request, nombreU, nombreP):
    
    ContactoPaseador.objects.filter(usuario=nombreU,paseador=nombreP).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Consulta efectuada', extra_tags="tag1")

    return redirect("notiContacto")