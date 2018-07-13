# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20180612_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('horror', 'Horror'), ('comedy', 'Comedy'), ('action', 'Action'), ('drama', 'Drama')], max_length=10)),
            ],
        ),
    ]
