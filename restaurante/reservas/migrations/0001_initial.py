# Generated by Django 5.1.1 on 2024-10-08 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peticion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('dia_reserva', models.DateField()),
                ('num_personas', models.IntegerField()),
                ('observaciones', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_reserva', models.CharField(max_length=200)),
                ('peticion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.peticion')),
            ],
        ),
    ]
