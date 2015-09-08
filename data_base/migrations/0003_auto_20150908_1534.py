# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0002_auto_20150908_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='AccessionNumber',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='PatientBirthTime',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='PatientBirthdate',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='SeriesDescription',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
    ]
