# Generated by Django 5.1.2 on 2024-10-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0033_remove_platos_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bebidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_bebida', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Bebida',
                'verbose_name_plural': 'Bebidas',
            },
        ),
    ]