# Generated by Django 5.1.3 on 2024-12-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0068_alter_mispedidos_plato_alter_perfil_tel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebidas',
            name='valoracion',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=0),
        ),
        migrations.AlterField(
            model_name='valoracion',
            name='valoracion',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')]),
        ),
        migrations.AlterField(
            model_name='valoracionplato',
            name='valoracion',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')]),
        ),
    ]
