# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0005_auto_20180614_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='KMH',
            field=models.DecimalField(decimal_places=10, null=True, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Lat',
            field=models.DecimalField(decimal_places=10, null=True, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='Lon',
            field=models.DecimalField(decimal_places=10, null=True, max_digits=10),
        ),
    ]
