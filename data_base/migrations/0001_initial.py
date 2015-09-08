# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('SeriesNumber', models.CharField(max_length=200)),
                ('SeriesInstanceUID', models.CharField(max_length=200)),
                ('ProtocolName', models.CharField(max_length=200)),
                ('Modality', models.CharField(max_length=200)),
                ('AccessionNumber', models.CharField(default='', max_length=200)),
                ('SeriesDescription', models.CharField(default='', max_length=200)),
                ('SeriesTime', models.CharField(default='', max_length=200)),
                ('ContrastAgent', models.CharField(default='', max_length=200)),
                ('ScanningSequence', models.CharField(default='', max_length=200)),
                ('BodyPartExaminated', models.CharField(default='', max_length=200)),
                ('AcquisitionNumber', models.CharField(default='', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MR_Params',
            fields=[
                ('PixelSpacing', models.CharField(default='', max_length=200)),
                ('SliceThickness', models.CharField(default='', max_length=200)),
                ('EchoTime', models.CharField(default='', max_length=200)),
                ('EchoNumbers', models.CharField(default='', max_length=200)),
                ('InversionTime', models.CharField(default='', max_length=200)),
                ('RepetitionTime', models.CharField(default='', max_length=200)),
                ('modality_params', models.OneToOneField(to='data_base.Series', primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CT_Params',
            fields=[
                ('Name', models.CharField(default='', max_length=200)),
                ('modality_params', models.OneToOneField(to='data_base.Series', primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('StudyDescription', models.CharField(max_length=200)),
                ('StationName', models.CharField(max_length=200)),
                ('ManufacturerModelName', models.CharField(max_length=200)),
                ('StudyInstanceUID', models.CharField(max_length=200)),
                ('Pathology', models.CharField(default='', max_length=200)),
                ('StudyDate', models.CharField(default='', max_length=200)),
                ('StudyTime', models.CharField(default='', max_length=200)),
                ('AccessionNumber', models.CharField(default='', max_length=200)),
                ('InstitutionName', models.CharField(default='', max_length=200)),
                ('ReferringPhysicianName', models.CharField(default='', max_length=200)),
                ('PerformingPhysicianName', models.CharField(default='', max_length=200)),
                ('ModalitiesInStudy', models.CharField(default='', max_length=200)),
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
                ('Name', models.CharField(default='', max_length=200)),
                ('modality_params', models.OneToOneField(to='data_base.Series', primary_key=True, serialize=False)),
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
    ]
