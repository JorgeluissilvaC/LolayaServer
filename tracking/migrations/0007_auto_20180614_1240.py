# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0006_auto_20180614_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracking',
            name='AlertaID',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='Emergencia',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='IdGeocerca',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='pasajeros',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='ConduccionDeHorasMetros',
            field=models.DecimalField(max_digits=10, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='DistanciaRecorrida',
            field=models.DecimalField(max_digits=10, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='KMH',
            field=models.DecimalField(max_digits=10, null=True, decimal_places=8),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Lat',
            field=models.DecimalField(max_digits=10, null=True, decimal_places=8),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Lon',
            field=models.DecimalField(max_digits=10, null=True, decimal_places=8),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='ValorADC',
            field=models.DecimalField(max_digits=10, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='ValorEntradasYsalidas',
            field=models.DecimalField(max_digits=10, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='VolInterno',
            field=models.DecimalField(max_digits=10, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='VoltajePrincipal',
            field=models.DecimalField(max_digits=10, null=True, decimal_places=2),
        ),
    ]
