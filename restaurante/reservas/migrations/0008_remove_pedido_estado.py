# Generated by Django 5.1.1 on 2024-10-08 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0007_rename_cliente_pedido_nombre_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='estado',
        ),
    ]
