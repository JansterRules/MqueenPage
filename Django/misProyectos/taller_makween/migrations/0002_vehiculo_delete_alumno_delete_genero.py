# Generated by Django 4.1.2 on 2024-06-09 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller_makween', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('placa', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('año', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
    ]
