from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'paginas/index.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def listarAlgo(request):
    context = Perro.objects.all()
    return render(request, 'paginas/listarAlgo.html', {'context': context})

def agregarAlgo(request):
    form = Perro_form(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    render(request, 'paginas/formulario.html', {'context':form})