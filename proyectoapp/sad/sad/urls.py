"""
URL configuration for sad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from deportistas.views import agregar_deportista, ver_deportista, editar_deportista, eliminar_deportista
from webapp.views import mostrar_deportistas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_deportistas, name='inicio'),
    path('agregar_deportista/', agregar_deportista),
    path('ver_deportista/<int:idDeportista>', ver_deportista),
    path('editar_deportista/<int:idDeportista>', editar_deportista),
    path('eliminar_deportista/<int:idDeportista>', eliminar_deportista),
]
