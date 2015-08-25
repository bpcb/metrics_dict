# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0008_remove_metric_metric_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definition',
            name='end_date',
            field=models.DateField(default=None, null=True, verbose_name=b'Definition end date', blank=True),
        ),
    ]
