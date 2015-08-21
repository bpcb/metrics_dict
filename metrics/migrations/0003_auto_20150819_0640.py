# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0002_metric_metric_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='metric_text',
            field=models.TextField(max_length=500),
        ),
    ]
