from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse
from itertools import chain
from datetime import date as dt
from datetime import *
import locale
from django.db.models import Q
from calendar import monthrange

#Declarar funciones para hacer cuando se ingresan direcciones

# Create your views here.
usuario = {
    "nombre": "",
    "esCliente": False,
    "esVeterinario": False,
}
def getUsuario():
    return usuario

infoHistorial = {
    "nombre": "",
    "nombreP": "",
    "mailD": "",
}

def index(request):
    context ={
        'usuario':usuario
    }
    return render(request, 'paginas/index.html', context)

def adopciones(request):
    context = {
        'usuario':usuario
    }
    return render(request, 'paginas/adopciones.html', context)

def adopFamilias(request, nombre, usu):
    adop = PerroAdopcion.objects.get(nombre=nombre,usuario=usu)
    adop.estado = True
    adop.save()
    messages.add_message(request, messages.SUCCESS, 'La publicación se agrego a adopciones realizadas ', extra_tags="tag1")

    perro_Adop = PerroAdopcion.objects.filter(estado = True)
    context = {'context': perro_Adop,
               'usuario': usuario,
               }
    return render(request, 'paginas/adopFamilias.html', context)

def adopflias(request):

    perro_Adop = PerroAdopcion.objects.filter(estado = True)
    context = {'context': perro_Adop,
               'usuario': usuario,
               }
    return render(request, 'paginas/adopFamilias.html', context)

def borrarAdoptado(request, usuario, nombre):
    perro = PerroAdopcion.objects.get(usuario=usuario, nombre=nombre)
    perro.estado = False
    perro.save()
    messages.add_message(request, messages.SUCCESS, 'La publicación se elimino con éxito y se agrego nuevamente en perros en adopción ', extra_tags="tag1")

    return redirect('listarAdopciones')





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
            p=Perro.objects.filter(nombre=form.cleaned_data['nombre'], emailDueño=usr.mail).exists()
            if p:
                messages.add_message(request, messages.SUCCESS, 'El nombre del perro ya se encuentra registrado para ese dueño', extra_tags="tag1")
                return redirect('registrarPerro')
            edad = (datetime.now().year - form.cleaned_data['fechaNacimiento'].year)
            perro = Perro(
                nombre = form.cleaned_data['nombre'],
                raza = form.cleaned_data['raza'],
                edad = edad,
                emailDueño = usr.mail,
                sexo = form.cleaned_data['sexo'],
                tamaño = form.cleaned_data['tamaño'],
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


def borrarPerro(request, id):
    p = Perro.objects.get(id=id)
    usr = Cliente.objects.get(mail=p.emailDueño)
    PerroAdopcion.objects.filter(usuario=usr.usuario).delete()
    PerroPerdido.objects.filter(usuario=usr.usuario).delete()
    p.delete()
    messages.add_message(request, messages.SUCCESS, 'Perro Eliminado', extra_tags="tag1")
    
    return redirect("losPerros")

def borrarPerroA(request,usuario, nombre):
    perro = PerroAdopcion.objects.get(usuario=usuario, nombre=nombre)
    perro.delete()
    messages.add_message(request, messages.SUCCESS, 'la publicación se elimino con éxito', extra_tags="tag1")

    return redirect("listarAdopciones")



def borrarPerroC(request, id):
    p = Perro.objects.get(id=id)
    usr = Cliente.objects.get(mail=p.emailDueño)
    PerroAdopcion.objects.filter(usuario=usr.usuario).delete()
    PerroPerdido.objects.filter(usuario=usr.usuario).delete()
    p.delete()
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
    adop = PerroAdopcion.objects.filter(estado = False)
    context = {'context': adop,
               'usuario': usuario}
    return render(request, 'paginas/listarAdopciones.html', context)

def misPerros(request): 
    usu = Cliente.objects.get(usuario=usuario["nombre"])
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

def borrarC(request, id):
    Cuidador.objects.get(id=id).delete()
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

def borrarP(request, id):
    Paseador.objects.get(id=id).delete()
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
            t = Turnos.objects.filter(perro=form.cleaned_data['perro'],nombre=usr.nombreC).exists()
            if t:
                messages.add_message(request, messages.SUCCESS, 'Ya solicitaste turno para este perro', extra_tags="tag1")
                return redirect('turnos')
            turno = Turnos (
                descripcion = form.cleaned_data['descripcion'] ,
                nombre = usr.nombreC,
                edad = perro.edad,
                raza = perro.raza,
                perro = form.cleaned_data['perro'],
                sexo = perro.sexo,
                motivo = form.cleaned_data['motivo'],
                fecha = form.cleaned_data['fecha'],
                telDueño = usr.telefono,
                fHoraria = form.cleaned_data['fHoraria']
            )
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
    usu = Cliente.objects.get(usuario=usuario['nombre'])
    perros = Perro.objects.filter(emailDueño=usu.mail)
    listaPerros =["","Encontrado"]
    listaPerros += [p.nombre for p in perros]
    print(listaPerros)
    if request.method == 'POST':
        form = perroAdopcion_form(request.POST, request.FILES,opciones=listaPerros)
        if form.is_valid():
            
            d = Cliente.objects.get(usuario=usuario['nombre'])
            p = Perro.objects.filter(nombre=form.cleaned_data['nombre'], emailDueño=d.mail).exists()
            
            if not p:
                adop = PerroAdopcion(
                usuario = usuario['nombre'],
                nombre = 'Desconocido',
                raza = 'Desconocido',
                tamaño = 'Desconocido',
                descripcion = form.cleaned_data['descripcion'],
                zona = form.cleaned_data['zona'],
                edad = 0,
            )
            else:
                p = Perro.objects.get(nombre=form.cleaned_data['nombre'], emailDueño=d.mail)
                perroEx = PerroAdopcion.objects.filter(usuario=usuario['nombre'],nombre=p.nombre).exists()
                if perroEx:
                    messages.add_message(request, messages.SUCCESS, 'Ya publicaste esta adopcion', extra_tags="tag1")
                    return redirect('publicarAdopcion')
                adop = PerroAdopcion(
                    usuario = usuario['nombre'],
                    nombre = p.nombre,
                    raza = p.raza,
                    tamaño = p.tamaño,
                    descripcion = form.cleaned_data['descripcion'],
                    zona = form.cleaned_data['zona'],   
                    edad = p.edad,
                )
            
            adop.save()
            messages.add_message(request, messages.SUCCESS, 'Se ha publicado perro en adopcion ', extra_tags="tag1")

            return redirect("index")
    else:
         form = perroAdopcion_form( opciones=listaPerros)
    
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
    PerroAdopcion.objects.filter(usuario=cli.usuario).delete()
    
    PerroPerdido.objects.filter(usuario=cli.usuario).delete()
    Perro.objects.filter(emailDueño=cli.mail).delete()
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
    turnosPendientes = Turnos.objects.filter(estado = "pendiente")
    turnosConfirmados = Turnos.objects.filter(estado = "confirmado")
    turnosRechazados = Turnos.objects.filter(estado = "rechazado")
    context ={
        'usuario':usuario,
        'turnosC':turnosConfirmados,
        'turnosR':turnosRechazados,
        'turnosP':turnosPendientes,
    }
    return render(request,'paginas/notiTurnos.html', context)

def notiTurnosC(request):
    
    turnosPendientes = Turnos.objects.filter(estado = "pendiente",nombre = usuario['nombre'])
    turnosConfirmados = Turnos.objects.filter(estado = "confirmado",nombre = usuario['nombre'])
    turnosRechazados = Turnos.objects.filter(estado = "rechazado",nombre = usuario['nombre'])
    context ={
        'usuario':usuario,
        'turnosC':turnosConfirmados,
        'turnosR':turnosRechazados,
        'turnosP':turnosPendientes,
    }
    return render(request,'paginas/notiTurnosC.html', context)

def borrarNotiT(request, nombre, perro,descripcion):
    
    tur=Turnos.objects.get(nombre=nombre, perro=perro,descripcion=descripcion)
    tur.estado="confirmado"
    tur.save()
    messages.add_message(request, messages.SUCCESS, 'Confirmacion efectuado', extra_tags="tag1")

    return redirect('notiTurnos')

def borrarNotiTe(request, nombre, perro,descripcion,motivoRechazo):
    
    tur=Turnos.objects.get(nombre=nombre, perro=perro,descripcion=descripcion)
    tur.estado="rechazado"
    tur.motivoRechazo=motivoRechazo
    tur.save()
    messages.add_message(request, messages.SUCCESS, 'Rechazo efectuado', extra_tags="tag1")

    return redirect('notiTurnos')



def terminarContactoC(request, id):
    
    ContactoCuidador.objects.get(id=id).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Consulta efectuada', extra_tags="tag1")

    return redirect("notiContacto")

def terminarContactoP(request, id):
    
    ContactoPaseador.objects.get(id=id).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Consulta efectuada', extra_tags="tag1")

    return redirect("notiContacto")


def ContactarAdop(request, nombre, dueño):
    cli =  Cliente.objects.get(usuario=usuario["nombre"])
    existe = ContactoAdop.objects.filter(nombre=nombre,telUsuario=cli.telefono).exists()
    if existe:
        messages.add_message(request, messages.SUCCESS, 'Ya has contactado a este Dueño', extra_tags="tag1")
        return redirect("listarAdopciones")
    adopcion = ContactoAdop(
        nombre =  nombre,
        dueño=dueño,
        usuario = cli.nombreC,
        telUsuario = cli.telefono,
    )
    
    adopcion.save()
    messages.add_message(request, messages.SUCCESS, 'Pronto se pondran en contacto con usted', extra_tags="tag1")
    return redirect("index")

def contactarAVisit(request, nombre, dueño):
    if request.method == 'POST':
        form = contacto_form(request.POST) 
        if form.is_valid():
            contactoNuevo = ContactoAdop(
                nombre = nombre,
                dueño=dueño,
                usuario = form.cleaned_data.get('usuario'),
                telUsuario = form.cleaned_data.get('telefono')
            )
            contactoNuevo.save()
            messages.add_message(request, messages.SUCCESS, 'Pronto se pondran en contacto con usted', extra_tags="tag1")
            return redirect ('index')
    else:
        form = contacto_form()
    context = {
        'usuario' : usuario,
        'form' : form,
        'nombre' : nombre,
        'dueño' : dueño,
    }

    return render(request, 'paginas/contactarAVisitante.html', context)
            
def listarPerdidos(request):
    perdidos = PerroPerdido.objects.filter(~Q(usuario=usuario["nombre"]), estado="perdido")
    #perdidos = PerroPerdido.objects.filter(estado="perdido")
    context = {
        'context':perdidos,
        'usuario':usuario,
    }
    return render(request, 'paginas/listaPerdidos.html', context)

def listarPerdidosEncontrados(request):
    perdidos = PerroPerdido.objects.filter(estado="encontrado")
    context = {
        'context':perdidos,
        'usuario':usuario,
    }
    return render(request, 'paginas/listarPerdidosEncontrados.html', context)

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
                perroEx = PerroPerdido.objects.filter(usuario=usuario['nombre'],nombre=p.nombre).exists()
                if perroEx:
                    messages.add_message(request, messages.SUCCESS, 'Ya publicaste esta desaparicion', extra_tags="tag1")
                    return redirect('publicarPerdido')
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

def borrarPerroPerdido(request, id):
    PerroPerdido.objects.get(id=id).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Perdida borrada', extra_tags="tag1")

    return redirect("index")

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
                telEncontro = form.cleaned_data.get('telefono'),
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
        'telDueño':telDueño,  
        }
    return render(request, 'paginas/contactarPerdVisit.html', context)

def encontrado(request, id):
    perro = PerroPerdido.objects.get(id=id)
    perro.estado="encontrado"
    perro.save()
    return redirect("misPerdidos")

def notificacionAdopcion(request):
    context ={
        'usuario':usuario
    }
    return render(request,'paginas/notificacionAdopcion.html', context)
    
def notiAdopContacto(request):
    cli = Cliente.objects.get(usuario = usuario["nombre"])
    noti = ContactoAdop.objects.filter(dueño=cli.usuario)
    context ={
        'usuario':usuario,
        'context': noti,
    }
    return render(request,'paginas/notiAdopContactos.html', context)

def eliminarContactoA(request, usuario, nombre):
    
    ContactoAdop.objects.filter(usuario=usuario,nombre=nombre).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Consulta efectuada', extra_tags="tag1")

    return redirect("notiAdopContacto")

def calendar(request):
    mes=dt.today().month
    #locale.setlocale(locale.LC_TIME, 'es_ES')
    mes=dt.today().strftime('%B').capitalize()
    
    events = Event.objects.all().order_by('date')
    fecha = Event.objects.filter(date__month = dt.today().month).order_by('date')
    
    dicc = {}
    cantidad_dias = monthrange(2023, dt.today().month)[1]
    #print(cantidad_dias)
    for i in range(cantidad_dias):
        dicc[i+1] = []
    #print(dicc)
    for f in fecha:
        dicc[f.date.day].append(f'{f.title}, {f.description}')  
    return render(request, 'paginas/calendar.html', 
                  {'mes':mes,'fecha': dicc, 'events': events,'usuario':usuario})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Veterinaria de Turno Agregada', extra_tags="tag1")
            return redirect('calendar')
    else:
        form = EventForm()
    return render(request, 'paginas/add_event.html', {'form': form, 'usuario': usuario})

def delete_event(request, event_id):
    Event.objects.get(pk=event_id).delete()
    messages.add_message(request, messages.SUCCESS, 'Veterinaria de Turno eliminada', extra_tags="tag1")
    return redirect('calendar')

"""      
  'nombre' : nombre,
        'telDueño' : telDueño,    
        }
    return render(request, 'paginas/contactarPerdVisit.html', context)
"""

def notiPerdidos(request):
    cli =  Cliente.objects.get(usuario=usuario["nombre"])
    noti = ContactoPerdido.objects.filter(telDueño=cli.telefono)
    context = {
        'context' : noti,
        'usuario' : usuario,
    }
    return render(request, 'paginas/notiPerdidos.html', context)

def terminarPerd(request, id):
    ContactoPerdido.objects.get(id=id).delete()
    
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
    return render(request,'paginas/misPerdidos.html',context)


def listarHistorialV(request,nombre):
    his = Historial.objects.all().filter(nombreP=nombre)
    print (nombre)
    context = {
        'context':his,
        'usuario':usuario
    }
    return render(request, 'paginas/listarHistorialV.html', context)

def validate(request):#extrae el nombre y email del perro y hace de conector con los historiales y su creacion
   if request.method == 'POST':
      nombre= request.POST["nombre"]#tendria que ser un GET pero bueno, funciona
      emailD = request.POST["emailD"]
      infoHistorial['nombreP']= request.POST["nombre"]
      infoHistorial['mailD']= request.POST["emailD"]
      his = Historial.objects.filter(nombreP=nombre,mailD=emailD)
      cli=Cliente.objects.get(mail=emailD)
      context = {
        'context':his,
        'usuario':usuario,
        'nombreP':nombre,
        'nombreC':cli.nombreC
    }
      return render(request, 'paginas/listarHistorialV.html', context)#aca me tendria que mandar a listarHistorialV


def validateC(request):#extrae el nombre y email del perro y hace de conector con los historiales y su creacion
   if request.method == 'POST':
      nombre= request.POST["nombre"]#tendria que ser un GET pero bueno, funciona
      emailD = request.POST["emailD"]
      infoHistorial['nombreP']= request.POST["nombre"]
      infoHistorial['mailD']= request.POST["emailD"]
      his = Historial.objects.all().filter(nombreP=nombre,mailD=emailD)
      cli=Cliente.objects.get(mail=emailD)
      context = {
        'context':his,
        'usuario':usuario,
        'nombreP':nombre,
        'nombreC':cli.nombreC
    }
      return render(request, 'paginas/listarHistorialC.html', context)


def listarHistorialC(request):
    his = Historial.objects.all().filter(nombreP=infoHistorial['nombreP'], mailD= infoHistorial['mailD'])
    context = {
        'context':his,
        'usuario':usuario
    }
    return render(request, 'paginas/listarHistorialC.html', context)




def cargarHistorial(request):
    if request.method == 'POST':
        form = Historial_form(request.POST)
        if form.is_valid(): 
            prro = Perro.objects.get(nombre=infoHistorial['nombreP'], emailDueño=infoHistorial['mailD'])
            his = Historial(
                nombreP = prro.nombre,
                mailD = prro.emailDueño,
                raza = prro.raza,
                edad = prro.edad,
                descripcion = form.cleaned_data['descripcion'],
                fecha = form.cleaned_data['fecha'],
                castrado = form.cleaned_data['castrado'],
                pulsaciones  = form.cleaned_data['pulsaciones'],
                estudios_complementarios = form.cleaned_data['estudios_complementarios'],
                diagnostico_presuntivo = form.cleaned_data['diagnostico_presuntivo'],
                tratamiento = form.cleaned_data['tratamiento'],
                proxima_visita = form.cleaned_data['proxima_visita'],
            )
            print(his)
            his.save()
            messages.add_message(request, messages.SUCCESS, 'Historial cargado con exito', extra_tags="tag1")

            return redirect('losPerros')
    else:
        form = Historial_form()
            
    context = {

        'form': form,
        'usuario':usuario,
    }
    return render(request, 'paginas/cargarHistorial.html', context)
#hola



def donaciones(request):
    don = Donacion.objects.all()
    context = {
        'usuario':usuario,
        'context':don,
    }
    return render(request, 'paginas/donaciones.html', context)

def agregarDonac(request):
    if request.method == 'POST':
        form = Donacion_form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Donacion cargada con exito', extra_tags="tag1")
            return redirect("donaciones")
    else:
        form = Donacion_form()
    context = {
        'usuario': usuario,
        'form': form,
    }
    return render(request, 'paginas/agregarDonac.html', context)

def borrarDonac(request, id):
    Donacion.objects.get(id=id).delete()
    
    messages.add_message(request, messages.SUCCESS, 'Colecta borrada', extra_tags="tag1")

    return redirect("donaciones")

def donar(request, id):
    if request.method == 'POST':
        form = Tarjeta_form(request.POST)
        if form.is_valid():
            donacion = Donacion.objects.get(id=id)
            x = donacion.recaudado + form.cleaned_data[0]
            donacion.recaudado = x
            donacion.progreso = donacion.recaudado * 100 / donacion.objetivo
            donacion.save()
            tarjeta = Tarjeta.objects.get(numero=form.cleaned_data[1])
            x = tarjeta.saldo - form.cleaned_data[0]
            tarjeta.saldo = x
            tarjeta.save()
            messages.add_message(request, messages.SUCCESS, 'Gracias por contribuir', extra_tags="tag1")
            return redirect("donaciones")
    else:
        form = Tarjeta_form()
    context = {
        'usuario': usuario,
        'form': form,
        'id':id,
    }
    return render(request, 'paginas/pagarConTarjeta.html', context)
    
    
