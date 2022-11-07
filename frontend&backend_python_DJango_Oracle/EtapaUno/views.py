from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion
from . forms import PublicacionForm

# Create your views here.
def home(request):

    publicaciones= Publicacion.objects.all()
    
    return render(request, 'index.html', context={'datos':publicaciones},)
   
def crearPublicacion(request):
    if request.method=='POST':
        publicacion = PublicacionForm(request.POST)
        if publicacion.is_valid():
            publicacion.save()
        return redirect('home')
    else:
        publicacion=PublicacionForm()
        return render(request, 'EtapaUno/form_publicacion.html', {'publicacion':publicacion})

def form_mod_publicacion(request,id):
    publicacion = Publicacion.objects.get(id=id)

    datos ={
        'form': PublicacionForm(instance=publicacion)
    }
    if request.method == 'POST':
        formulario = PublicacionForm(data=request.POST, instance = publicacion)
        if formulario.is_valid:
            formulario.save()
            return redirect('home')
    return render(request, 'EtapaUno/form_mod_publicacion.html', datos)

def form_del_publicacion(request,id):
    publicacion = Publicacion.objects.get(id=id)
    publicacion.delete()
    return redirect('home')

def galeria(request):
    return render(request, 'galeria.html')