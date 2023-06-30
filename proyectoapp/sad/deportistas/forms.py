from django.forms import ModelForm

from deportistas.models import Deportista
class DeportistaFormulario(ModelForm):

    class Meta:
        model = Deportista
        fields = ('nombre', 'apellido', 'cedula', 'sexo', 'edad', 'disciplina', 'ciudad', 'sede', 'competencia')