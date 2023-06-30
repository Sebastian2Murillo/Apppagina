from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader
from deportistas.forms import DeportistaFormulario
from deportistas.models import Deportista

# Create your views here.
def agregar_deportista(request):
    pagina = loader.get_template('agregar_deportista.html')
    if request.method == 'GET':
        formulario = DeportistaFormulario
    elif request.method =='POST':
        formulario = DeportistaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos,request))


def ver_deportista (request, idDeportista):
    pagina = loader.get_template('ver_deportista.html')
    deportista = get_object_or_404(Deportista, pk=idDeportista)
    mensaje = {'deportista': deportista}
    return HttpResponse(pagina.render(mensaje, request))


def editar_deportista(request,idDeportista):
    pagina = loader.get_template('editar_deportista.html')
    deportista = get_object_or_404(Deportista, pk=idDeportista)
    if request.method == 'GET':
        formulario = DeportistaFormulario(instance=deportista)
    elif request.method =='POST':
        formulario = DeportistaFormulario(request.POST, instance=deportista)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    mensaje = {'formulario': formulario}
    return HttpResponse(pagina.render(mensaje, request))


def eliminar_deportista(request,idDeportista):
    deportista = get_object_or_404(Deportista, pk=idDeportista)
    if deportista:
        deportista.delete()
        return redirect('inicio')