# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0003_auto_20150828_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='status',
            new_name='progress',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='progress',
        ),
        migrations.AddField(
            model_name='feed',
            name='status',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
