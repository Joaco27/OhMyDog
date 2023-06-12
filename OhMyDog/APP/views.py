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
            usr=Cliente.objects.get(usuario=usuario['nombre'])
            perro = Perro(
                nombre = form.cleaned_data['nombre'],
                raza = form.cleaned_data['raza'],
                edad = form.cleaned_data['edad'],
                emailDueño = usr.mail,
            )
            perro.save()
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
            usr=Cliente.objects.get(usuario=form.cleaned_data["usuario"])
            #usr.onLine = True
            usr.save()
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
    usr=Cliente.objects.get(usuario=usuario["nombre"])
    #usr.onLine = False
    usr.save()
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
    return render(request, 'paginas/listarAdopciones.html', context)

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
    existe = ContactoCuidador.objects.filter(telCuidador=telefono,telUsuario=cli.telefono).exists()
    if existe:
        messages.add_message(request, messages.SUCCESS, 'Ya has contactado a este Cuidador', extra_tags="tag1")
        return redirect("cuidadores")
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
    context = {
        'form': form,
        'usuario':usuario,
        'nombre' : nombre,
        'telefono' : telefono,    
        }
    return render(request, 'paginas/contactarCVisitante.html', context)

def contactarP(request, nombre, telefono):
    cli =  Cliente.objects.get(usuario=usuario["nombre"])
    existe = ContactoPaseador.objects.filter(telPaseador=telefono,telUsuario=cli.telefono).exists()
    if existe:
        messages.add_message(request, messages.SUCCESS, 'Ya has contactado a este Paseador', extra_tags="tag1")
        return redirect("paseadores")
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
    usr = Cliente.objects.get(usuario=usuario['nombre'])
    perros = Perro.objects.filter(emailDueño=usr.mail)
    listaPerros =[""]
    listaPerros += [p.nombre for p in perros]
    if request.method == 'POST':
        form = Turnos_form(request.POST, opciones=listaPerros)
        if form.is_valid():
            perro=Perro.objects.get(nombre=form.cleaned_data['perro'],emailDueño=usr.mail)
            form.save()#primero guardo el form como viene (con los fields en null)
            #despues lo vuelvo a traer y seteo lo que quiero
            #como no deja modificar el form. hasta que este guardado, encontre esta solu
            turno = Turnos.objects.get(descripcion=form.cleaned_data['descripcion'],perro=form.cleaned_data['perro'])
            turno.nombre=usr.usuario
            turno.raza=perro.raza
            turno.edad=perro.edad
            turno.save()
            messages.add_message(request, messages.SUCCESS, 'El veterinario se pondra en contacto pronto', extra_tags="tag1")

            return redirect("index")
    else:
        form = Turnos_form(opciones=listaPerros)
    perros=Perro.objects.filter(emailDueño=usr.mail)
    print (perros)
    context = {
        'form': form,
        'usuario' : usuario,
        'perros' : perros
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
    if PerroAdopcion.objects.filter(usuario=cli.usuario).exists():
        adopciones = PerroAdopcion.objects.get(usuario=cli.usuario)
        adopciones.delete()
    if Perro.objects.filter(emailDueño=cli.mail).exists():
        perros = Perro.objects.get(emailDueño=cli.mail)
        perros.delete()
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

def notiTurnos(request):
    turnos = Turnos.objects.all()
    #d = chain(datosC,datosP)s
    context ={
        'usuario':usuario,
        'turnos':turnos,
    }
    return render(request,'paginas/notiTurnos.html', context)

def borrarNotificacionT(request, nombreU):
    
    Turnos.objects.filter(usuario=nombreU).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Consulta efectuada', extra_tags="tag1")

    return redirect("notiTurnos")

def terminarContactoC(request, nombreU, nombreC):
    
    ContactoCuidador.objects.filter(usuario=nombreU,cuidador=nombreC).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Consulta efectuada', extra_tags="tag1")

    return redirect("notiContacto")

def terminarContactoP(request, nombreU, nombreP):
    
    ContactoPaseador.objects.filter(usuario=nombreU,paseador=nombreP).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Consulta efectuada', extra_tags="tag1")

    return redirect("notiContacto")

def listarPerdidos(request):
    perdidos = PerroPerdido.objects.all()
    context = {
        'context':perdidos,
        'usuario':usuario
    }
    return render(request, 'paginas/listaPerdidos.html', context)

def publicarPerdido(request):
    usu = Cliente.objects.get(usuario=usuario['nombre'])
    perros = Perro.objects.filter(emailDueño=usu.mail)
    listaPerros =["","Encontrado"]
    listaPerros += [p.nombre for p in perros]
    print(listaPerros)
    if request.method == 'POST':
        form = perroPerdido_form(request.POST, request.FILES,opciones=listaPerros)
        if form.is_valid():
            
            d = Cliente.objects.get(usuario=usuario['nombre'])
            p = Perro.objects.filter(nombre=form.cleaned_data['nombre'], emailDueño=d.mail).exists()
            
            if not p:
                perdido = PerroPerdido(
                usuario = usuario['nombre'],
                dueño = d.nombreC,
                telDueño = usu.telefono,
                nombre = 'Desconocido',
                raza = 'Desconocido',
                descripcion = form.cleaned_data['descripcion'],
                zona = form.cleaned_data['zona'],
                fechaD = form.cleaned_data['fechaD'],
                imagen = form.cleaned_data['imagen'],
            )
            else:
                p = Perro.objects.get(nombre=form.cleaned_data['nombre'], emailDueño=d.mail)
                perdido = PerroPerdido(
                    usuario = usuario['nombre'],
                    dueño = d.nombreC,
                    telDueño = usu.telefono,
                    nombre = p.nombre,
                    raza = p.raza,
                    descripcion = form.cleaned_data['descripcion'],
                    zona = form.cleaned_data['zona'],
                    fechaD = form.cleaned_data['fechaD'],
                    imagen = form.cleaned_data['imagen'],
                )
            
            perdido.save()
            messages.add_message(request, messages.SUCCESS, 'Se ha publicado la desaparicion', extra_tags="tag1")

            return redirect("index")
    else:
        form = perroPerdido_form( opciones=listaPerros)
    
    context = {
        'form': form,
        'usuario' : usuario,
    }
    return render(request, 'paginas/publicarPerdido.html', context)

def borrarPerroPerdido(request, dueño, nombre):
    PerroPerdido.objects.filter(dueño=dueño,nombre=nombre).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Perdida borrada', extra_tags="tag1")

    return redirect("listarPerdidos")

def contactarPerd(request, nombre, telDueño):
    cli =  Cliente.objects.get(usuario=usuario["nombre"])
    existe = ContactoPerdido.objects.filter(telDueño=telDueño,telEncontro=cli.telefono,nombreP=nombre).exists()
    if existe:
        messages.add_message(request, messages.SUCCESS, 'Ya has reportado a este perro', extra_tags="tag1")
        return redirect("listarPerdidos")
    perd = ContactoPerdido(
        nombreP =  nombre,
        telDueño = telDueño,
        encontro = cli.nombreC,
        telEncontro = cli.telefono,
    )
    perd.save()
    messages.add_message(request, messages.SUCCESS, 'Le informaremos al Dueño', extra_tags="tag1")
    return redirect("index")

def contactarPerdVisit(request, nombre, telDueño):
    if request.method == 'POST':
        form = contacto_form(request.POST) 
        if form.is_valid():
            contactoNuevo = ContactoPerdido(
                nombreP = nombre,
                telDueño = telDueño,
                encontro = form.cleaned_data.get('usuario'),
                telEncontro = form.cleaned_data.get('telefono')
            )
            contactoNuevo.save()
            messages.add_message(request, messages.SUCCESS, 'Le informaremos al Dueño', extra_tags="tag1")

            return redirect("index")
    else:
        form = contacto_form()
    context = {
        'form': form,
        'usuario':usuario,
        'nombre' : nombre,
        'telDueño' : telDueño,    
        }
    return render(request, 'paginas/contactarPerdVisit.html', context)

def notiPerdidos(request):
    cli =  Cliente.objects.get(usuario=usuario["nombre"])
    noti = ContactoPerdido.objects.filter(telDueño=cli.telefono)
    context = {
        'context' : noti,
        'usuario' : usuario,
    }
    return render(request, 'paginas/notiPerdidos.html', context)

def terminarPerd(request, nombreP, encontro):
    ContactoPerdido.objects.filter(nombreP=nombreP,encontro=encontro).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Reporte efectuada', extra_tags="tag1")

    return redirect("notiPerdidos")

def publicaciones(request):
    context = {
        'usuario' : usuario,
    }
    return render(request,'paginas/publicaciones.html', context)

def misPerdidos(request):
    perd = PerroPerdido.objects.filter(usuario=usuario['nombre'])
    context = {
        'context' : perd,
        'usuario' : usuario,
    }
    return render(request,'paginas/misperdidos.html',context)