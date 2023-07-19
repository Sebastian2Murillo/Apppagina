from django.db import models

# Create your models here.

class Sede(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    encargado = models.CharField(max_length=50, null=True)
    direccion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.nombre}'


class Competencia(models.Model):
    categoria = models.CharField(max_length=50, null=True)
    torneo = models.CharField(max_length=50, null=True)
    lugar = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.categoria}'

class Representante(models.Model):

    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    nombre_representante = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(null=True, max_length=10)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    telefono = models.CharField(null=True, max_length=10)
    def __str__(self):
        return f'{self.nombre_representante}'



class Deportista(models.Model):
    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(null=True, max_length=10)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True)
    edad = models.IntegerField(null=True)
    disciplina = models.CharField(null=True, max_length=50)
    ciudad = models.CharField(null=True, max_length=50)
    activo = models.BooleanField(default=True)
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True)
    competencia = models.ForeignKey(Competencia, on_delete=models.SET_NULL, null=True)
    representante = models.ForeignKey(Representante, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'id: {self.id} - {self.nombre} {self.apellido}'