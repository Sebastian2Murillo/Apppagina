from django.contrib import admin
from deportistas.models import Deportista, Sede, Competencia

# Register your modes here.
admin.site.register(Deportista)
admin.site.register(Sede)
admin.site.register(Competencia)