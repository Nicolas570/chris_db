# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0003_auto_20150908_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ct_params',
            name='Name',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='us_params',
            name='Name',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
    ]
