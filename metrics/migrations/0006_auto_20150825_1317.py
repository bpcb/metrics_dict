# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0005_metric_metric_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sql', models.TextField(max_length=1000)),
                ('start_date', models.DateField(default=datetime.date(2015, 8, 25), verbose_name=b'Definition start date')),
                ('end_date', models.DateField(default=None, null=True, verbose_name=b'Definition end date')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='metric',
            name='update_date',
        ),
        migrations.AddField(
            model_name='definition',
            name='metric',
            field=models.ForeignKey(to='metrics.Metric'),
        ),
    ]
