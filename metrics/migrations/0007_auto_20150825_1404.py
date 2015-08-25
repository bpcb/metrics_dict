# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0006_auto_20150825_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metric',
            name='experience',
        ),
        migrations.AddField(
            model_name='definition',
            name='experience',
            field=models.CharField(default=b'All', max_length=10, choices=[(b'ALL', b'All'), (b'Desktop', b'Desktop'), (b'Phone', b'Phone'), (b'Tablet', b'Tablet'), (b'Web', b'Web'), (b'Apps', b'Apps')]),
        ),
    ]
