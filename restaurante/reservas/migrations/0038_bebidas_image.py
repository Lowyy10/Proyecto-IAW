# Generated by Django 5.1.2 on 2024-10-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0037_tipo_comida_alter_platos_ingredientes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bebidas',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
