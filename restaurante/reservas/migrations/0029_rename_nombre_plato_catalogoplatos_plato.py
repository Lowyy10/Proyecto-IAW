# Generated by Django 5.1.1 on 2024-10-10 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0028_rename_plato_catalogoplatos_nombre_plato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogoplatos',
            old_name='nombre_plato',
            new_name='plato',
        ),
    ]