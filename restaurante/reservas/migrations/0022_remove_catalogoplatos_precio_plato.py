# Generated by Django 5.1.1 on 2024-10-09 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0021_catalogoplatos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogoplatos',
            name='precio_plato',
        ),
    ]
