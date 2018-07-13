# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Etiqueta', models.CharField(max_length=200)),
                ('idSensor', models.BigIntegerField()),
                ('versión', models.CharField(max_length=200)),
                ('Software', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('CodUbicación', models.CharField(max_length=200)),
                ('Lat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Lon', models.DecimalField(decimal_places=2, max_digits=5)),
                ('KMH', models.DecimalField(decimal_places=2, max_digits=5)),
                ('GradosDeRumbo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SatélitesUsados', models.BigIntegerField()),
                ('GPSCorrecto', models.BigIntegerField()),
                ('DistanciaRecorrida', models.DecimalField(decimal_places=2, max_digits=5)),
                ('VoltajePrincipal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ValorEntradasYsalidas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Modo', models.BigIntegerField()),
                ('NumeroReportesEnviados', models.BigIntegerField()),
                ('ConducciónDeHorasMetros', models.DecimalField(decimal_places=2, max_digits=5)),
                ('VolInterno', models.DecimalField(decimal_places=2, max_digits=5)),
                ('TiempoReal', models.BigIntegerField()),
                ('ValorADC', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
