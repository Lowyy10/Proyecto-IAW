# Generated by Django 5.1.2 on 2024-10-15 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0032_platos_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platos',
            name='tipo',
        ),
    ]