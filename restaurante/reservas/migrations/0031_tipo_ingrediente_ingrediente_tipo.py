# Generated by Django 5.1.2 on 2024-10-15 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0030_ingrediente_platos_ingredientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_ingrediente', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo ingrediente',
                'verbose_name_plural': 'Tipos de ingredientes',
            },
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes', to='reservas.tipo_ingrediente'),
        ),
    ]