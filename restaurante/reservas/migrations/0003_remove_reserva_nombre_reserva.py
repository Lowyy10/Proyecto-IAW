# Generated by Django 5.1.1 on 2024-10-08 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_reserva_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='nombre_reserva',
        ),
    ]