# Generated by Django 5.1.2 on 2024-11-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0054_mispedidos_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platos',
            name='comentarios',
        ),
        migrations.RemoveField(
            model_name='platos',
            name='valoracion',
        ),
        migrations.AddField(
            model_name='platos',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
