# Generated by Django 5.1.2 on 2024-11-19 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0064_alter_mispedidos_plato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mispedidos',
            name='plato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.platos'),
        ),
    ]
