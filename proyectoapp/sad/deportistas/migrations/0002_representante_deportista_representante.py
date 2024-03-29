# Generated by Django 4.2.2 on 2023-07-07 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deportistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_representante', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=10, null=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, null=True)),
                ('telefono', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='deportista',
            name='representante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='deportistas.representante'),
        ),
    ]
