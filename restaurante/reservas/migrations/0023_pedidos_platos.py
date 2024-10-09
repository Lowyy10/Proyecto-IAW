# Generated by Django 5.1.1 on 2024-10-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0022_remove_catalogoplatos_precio_plato'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='platos',
            field=models.ManyToManyField(related_name='pedidos', through='reservas.PedidoPlato', to='reservas.platos'),
        ),
    ]