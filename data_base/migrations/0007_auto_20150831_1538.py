# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0006_auto_20150831_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ct_params',
            old_name='series',
            new_name='modality_params',
        ),
        migrations.RenameField(
            model_name='mr_params',
            old_name='series',
            new_name='modality_params',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='patientid',
            new_name='PatientId',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='modality',
            new_name='Modality',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='pathology',
            new_name='Pathology',
        ),
        migrations.RenameField(
            model_name='us_params',
            old_name='series',
            new_name='modality_params',
        ),
    ]
