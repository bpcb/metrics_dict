# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='metric_name',
            field=models.CharField(default='HDP PVs', max_length=50),
            preserve_default=False,
        ),
    ]
