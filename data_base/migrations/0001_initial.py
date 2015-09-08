# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CT_Params',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Name', models.CharField(default='', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MR_Params',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('PixelSpacing', models.CharField(default='', max_length=200)),
                ('SliceThickness', models.IntegerField(default=0)),
                ('EchoTime', models.FloatField(default=0)),
                ('EchoNumber', models.IntegerField(default=0)),
                ('InversionTime', models.IntegerField(default=0)),
                ('RepetionTime', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('PatientId', models.CharField(max_length=200)),
                ('PatientName', models.CharField(default='', max_length=200)),
                ('PatientAge', models.CharField(default='', max_length=200)),
                ('PatientSex', models.CharField(default='', max_length=200)),
                ('PatientBirthDate', models.CharField(default='', max_length=200)),
                ('PatientBirthTime', models.CharField(default='', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Name', models.CharField(default='', max_length=200)),
                ('Comment', models.CharField(default='', max_length=200)),
                ('Rating', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('SeriesNumber', models.CharField(max_length=200)),
                ('SeriesInstanceUID', models.CharField(max_length=200)),
                ('ProtocolName', models.CharField(max_length=200)),
                ('Modality', models.CharField(max_length=200)),
                ('AccessionNumber', models.CharField(default='', max_length=200)),
                ('SeriesTime', models.CharField(default='', max_length=200)),
                ('ContrastAgent', models.CharField(default='', max_length=200)),
                ('ScanningSequence', models.CharField(default='', max_length=200)),
                ('SeriesDescription', models.CharField(default='', max_length=200)),
                ('BodyPartExaminated', models.CharField(default='', max_length=200)),
                ('AcquisitionNumber', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('StudyDescription', models.CharField(max_length=200)),
                ('Pathology', models.CharField(max_length=200)),
                ('StationName', models.CharField(max_length=200)),
                ('ManufacturerModelName', models.CharField(max_length=200)),
                ('StudyInstanceUID', models.CharField(max_length=200)),
                ('StudyDate', models.CharField(default='', max_length=200)),
                ('StudyTime', models.CharField(default='', max_length=200)),
                ('AccessionNumber', models.CharField(default='', max_length=200)),
                ('InstitutionName', models.CharField(default='', max_length=200)),
                ('ReferringPhysician', models.CharField(default='', max_length=200)),
                ('PerformingPhysiciansName', models.CharField(default='', max_length=200)),
                ('ModalitiesInStudy', models.CharField(default='', max_length=200)),
                ('BodyPartExaminated', models.CharField(default='', max_length=200)),
                ('MagneticFieldStrength', models.IntegerField(default=0)),
                ('patient', models.ForeignKey(to='data_base.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='US_Params',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Name', models.CharField(default='', max_length=200)),
                ('modality_params', models.OneToOneField(to='data_base.Series')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='series',
            name='study',
            field=models.ForeignKey(to='data_base.Study'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='serie',
            field=models.ForeignKey(to='data_base.Series'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='study',
            field=models.ForeignKey(to='data_base.Study'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mr_params',
            name='modality_params',
            field=models.OneToOneField(to='data_base.Series'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ct_params',
            name='modality_params',
            field=models.OneToOneField(to='data_base.Series'),
            preserve_default=True,
        ),
    ]
