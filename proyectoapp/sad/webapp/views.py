from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from deportistas.models import Deportista
# Create your views here.
def mostrar_deportistas(request):
    cantidad_deportistas = Deportista.objects.count()
    pagina = loader.get_template('deportistas.html')
    lista_deportistas = Deportista.objects.all()
    datos = {'cantidad': cantidad_deportistas, 'deportistas': lista_deportistas}
    return HttpResponse(pagina.render(datos, request))