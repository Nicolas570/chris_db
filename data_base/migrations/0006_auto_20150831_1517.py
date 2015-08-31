# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0005_auto_20150831_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='CT_Params',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('series', models.OneToOneField(to='data_base.Series')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MR_Params',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('SliceThickness', models.IntegerField(default=0)),
                ('EchoTime', models.FloatField(default=0)),
                ('InversionTime', models.IntegerField(default=0)),
                ('RepetionTime', models.IntegerField(default=0)),
                ('series', models.OneToOneField(to='data_base.Series')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='US_Params',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('series', models.OneToOneField(to='data_base.Series')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='data',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='nb_files',
            new_name='NbFiles',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='progress',
            new_name='Progress',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='time',
            new_name='Time',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='duration',
            new_name='Duration',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='status',
            new_name='Status',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='time',
            new_name='Time',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='visible',
            new_name='Visible',
        ),
        migrations.RenameField(
            model_name='group',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='age',
            new_name='PatientAge',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='birthdate',
            new_name='PatientBirthdate',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='name',
            new_name='PatientName',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='sex',
            new_name='PatientSex',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='comment',
            new_name='Comment',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='Rating',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='instanceUID',
            new_name='ProtocolName',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='protocol_name',
            new_name='SeriesInstanceUID',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='series_name',
            new_name='SeriesName',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='inversion_time',
            new_name='MagneticFieldStrength',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='instanceUID',
            new_name='ManufacturerModelName',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='manufacturer_name',
            new_name='StationName',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='station_name',
            new_name='StudyInstanceUID',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='color',
            new_name='Color',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='token',
            old_name='value',
            new_name='Value',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='Password',
        ),
        migrations.RemoveField(
            model_name='review',
            name='data',
        ),
        migrations.RemoveField(
            model_name='study',
            name='echo_time',
        ),
        migrations.RemoveField(
            model_name='study',
            name='magnetic_field_strenght',
        ),
        migrations.RemoveField(
            model_name='study',
            name='slice_thickness',
        ),
        migrations.AddField(
            model_name='review',
            name='study',
            field=models.ForeignKey(to='data_base.Study', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='study',
            name='modality',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
    ]
