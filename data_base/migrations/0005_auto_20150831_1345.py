# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0004_auto_20150828_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.BigIntegerField(max_length=20)),
                ('data', models.ForeignKey(to='data_base.Data')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='data',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='data_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='feed_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='group_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='dob',
            new_name='birthdate',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='gender',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='mrn',
            new_name='patientid',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='pathology',
            new_name='sex',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='protocol_name',
            new_name='instanceUID',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='series_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='study_name',
            new_name='pathology',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='membership',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patient_name',
        ),
        migrations.AddField(
            model_name='series',
            name='instanceUID',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='protocol_name',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
    ]
