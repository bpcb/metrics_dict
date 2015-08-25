# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0004_metric_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='metric_description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
