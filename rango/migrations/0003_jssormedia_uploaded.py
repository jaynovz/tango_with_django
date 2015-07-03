# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_jssormedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='jssormedia',
            name='uploaded',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
