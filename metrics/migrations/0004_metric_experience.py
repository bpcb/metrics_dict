# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0003_auto_20150819_0640'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='experience',
            field=models.CharField(default=b'All', max_length=10, choices=[(b'ALL', b'All'), (b'Desktop', b'Desktop'), (b'Phone', b'Phone'), (b'Tablet', b'Tablet'), (b'Web', b'Web'), (b'Apps', b'Apps')]),
        ),
    ]
