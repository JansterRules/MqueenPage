# Generated by Django 4.1.2 on 2024-07-09 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taller_makween', '0007_alter_carritoitem_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carritoitem',
            name='carrito',
        ),
        migrations.RemoveField(
            model_name='carritoitem',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
        migrations.DeleteModel(
            name='CarritoItem',
        ),
    ]