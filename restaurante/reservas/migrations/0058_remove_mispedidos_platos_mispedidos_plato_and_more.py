# Generated by Django 5.1.2 on 2024-11-12 17:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0057_remove_mispedidos_plato_mispedidos_platos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mispedidos',
            name='platos',
        ),
        migrations.AddField(
            model_name='mispedidos',
            name='plato',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservas.platos'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ValoracionPlato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.IntegerField(choices=[(0, '☆☆☆☆☆'), (1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')])),
                ('plato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valoraciones', to='reservas.platos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('plato', 'usuario')},
            },
        ),
        migrations.DeleteModel(
            name='PedidoPlato',
        ),
    ]
