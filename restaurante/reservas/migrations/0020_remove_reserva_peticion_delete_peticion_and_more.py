# Generated by Django 5.1.1 on 2024-10-09 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0019_remove_pedidos_plato_pedidoplato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='peticion',
        ),
        migrations.DeleteModel(
            name='Peticion',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
