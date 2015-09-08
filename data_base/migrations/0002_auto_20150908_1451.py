# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='ScaningSequence',
            new_name='ScanningSequence',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='performingPhysiciansName',
            new_name='PerformingPhysiciansName',
        ),
        migrations.AddField(
            model_name='mr_params',
            name='PixelSpacing',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
    ]
