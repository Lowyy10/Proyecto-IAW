# Generated by Django 5.1.1 on 2024-10-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0014_platos_alter_peticion_options_alter_reserva_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='platos',
            name='precio_plato',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
