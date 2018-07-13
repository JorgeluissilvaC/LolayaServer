# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_serie'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Serie',
        ),
        migrations.AlterField(
            model_name='tracking',
            name='CodUbicación',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='ConducciónDeHorasMetros',
            field=models.DecimalField(blank=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='DistanciaRecorrida',
            field=models.DecimalField(blank=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Etiqueta',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='GPSCorrecto',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='GradosDeRumbo',
            field=models.DecimalField(blank=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='KMH',
            field=models.DecimalField(blank=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Lat',
            field=models.DecimalField(blank=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Lon',
            field=models.DecimalField(blank=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Modo',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='NumeroReportesEnviados',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='SatélitesUsados',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Software',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='TiempoReal',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='ValorADC',
            field=models.DecimalField(blank=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='ValorEntradasYsalidas',
            field=models.DecimalField(blank=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='VolInterno',
            field=models.DecimalField(blank=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='VoltajePrincipal',
            field=models.DecimalField(blank=True, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='idSensor',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='versión',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
