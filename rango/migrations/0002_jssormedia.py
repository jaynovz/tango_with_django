# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JssorMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'jssor_media/')),
                ('alternate_file_name', models.CharField(max_length=200, null=True)),
                ('alt_text', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
