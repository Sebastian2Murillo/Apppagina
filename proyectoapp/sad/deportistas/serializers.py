#from django.contrib.auth.models import User
from rest_framework import serializers

#from deportistas.models import Deportista


from deportistas.models import Deportista, Competencia


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competencia
        #fields = ['nombre', 'apellido', 'cedula', 'sexo', 'edad', 'disciplina', 'ciudad', 'sede', 'competencia', 'representante']

        fields = ['categoria', 'torneo', 'lugar']