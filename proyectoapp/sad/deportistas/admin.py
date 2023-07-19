from django.contrib import admin
from deportistas.models import Deportista, Sede, Competencia, Representante

# Register your modes here.
admin.site.register(Deportista)
admin.site.register(Sede)
admin.site.register(Competencia)
admin.site.register(Representante)