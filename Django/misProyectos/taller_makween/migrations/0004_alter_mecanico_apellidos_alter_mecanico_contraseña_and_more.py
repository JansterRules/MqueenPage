# Generated by Django 4.1.2 on 2024-06-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller_makween', '0003_mecanico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecanico',
            name='apellidos',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='contraseña',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='nombres',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='rut',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
