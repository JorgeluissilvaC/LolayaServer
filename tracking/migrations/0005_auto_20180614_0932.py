# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_auto_20180614_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracking',
            old_name='CodUbicación',
            new_name='CodUbicacion',
        ),
        migrations.RenameField(
            model_name='tracking',
            old_name='versión',
            new_name='version',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='ConducciónDeHorasMetros',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='SatélitesUsados',
        ),
        migrations.AddField(
            model_name='tracking',
            name='ConduccionDeHorasMetros',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5),
        ),
        migrations.AddField(
            model_name='tracking',
            name='SatelitesUsados',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='DistanciaRecorrida',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='GPSCorrecto',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='GradosDeRumbo',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='KMH',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Lat',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Lon',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Modo',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='NumeroReportesEnviados',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='TiempoReal',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='ValorADC',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='ValorEntradasYsalidas',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='VolInterno',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='VoltajePrincipal',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=5),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='date',
            field=models.DateTimeField(null=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='idSensor',
            field=models.BigIntegerField(null=True),
        ),
    ]
