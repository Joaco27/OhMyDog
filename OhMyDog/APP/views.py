from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

#Declarar funciones para hacer cuando se ingresan direcciones

# Create your views here.
usuario = {
    "nombre": "",
    "contra": "",
    "esCliente": False,
    "esVeterinario": True,
}

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
    }
    return render(request, 'paginas/registrarCliente.html', context)

def LogIn(request):
    if request.method == 'POST':
        form = LogIn_form(request.POST) 
        if form.is_valid(): 
            usuario["nombre"] = form.cleaned_data["usuario"]
            usuario["contra"] = form.cleaned_data["contra"]
            usuario['esCliente'] = True
            if usuario['nombre'] == "Veterinario":
                usuario['esVeterinario'] = True
            messages.add_message(request, messages.SUCCESS, 'Iniciaste Sesion', extra_tags="tag1")

            return redirect("index")
    else:
        form = LogIn_form()
        
    context = {
        'form': form,
    }
    return render(request, 'paginas/LogIn.html', context)

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
    context = Cuidador.objects.all()
    return render(request, 'paginas/listaCuidadores.html', {'context': context})
    
def listarPaseadores(request): 
    context = Paseador.objects.all()
    return render(request, 'paginas/listaPaseadores.html', {'context': context})

def contactarC(request, nombre, telefono):
    cuida = ContactoCuidador(
        cuidador =  nombre,
        telCuidador = telefono,
        usuario = 'Pedro',
        telUsuario = 1234567,
    )
    cuida.save()
    messages.add_message(request, messages.SUCCESS, 'Pronto se pondran en contacto con usted', extra_tags="tag1")
    return redirect("index")

def contactarP(request, nombre, telefono): 
    pasea = ContactoPaseador(
        paseador =  nombre,
        telPaseador = telefono,
        usuario = 'Pedro',
        telUsuario = 1234567,
    )
    pasea.save()
    messages.add_message(request, messages.SUCCESS, 'Pronto se pondran en contacto con usted', extra_tags="tag1")
    return redirect("index")

def publicar(request):
    context ={
        'usuario':usuario
    }
    return render(request,'paginas/publicar.html', context)

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
    }
    return render(request, 'paginas/agregarCuidador.html', context)

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
    }
    return render(request, 'paginas/agregarPaseador.html', context)

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
    }
    return render(request, 'paginas/publicarAdopcion.html', context)