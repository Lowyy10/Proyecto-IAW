# Generated by Django 5.1.1 on 2024-10-08 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0008_remove_pedido_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='comida',
            field=models.CharField(max_length=200),
        ),
    ]