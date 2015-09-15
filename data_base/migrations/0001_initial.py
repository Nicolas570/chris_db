# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('GroupName', models.CharField(max_length=200, default='')),
                ('GroupId', models.CharField(max_length=200, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('PatientID', models.CharField(max_length=200)),
                ('PatientName', models.CharField(max_length=200, default='')),
                ('PatientAge', models.CharField(max_length=200, default='')),
                ('PatientSex', models.CharField(max_length=200, default='')),
                ('PatientBirthDate', models.CharField(max_length=200, default='')),
                ('PatientBirthTime', models.CharField(max_length=200, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200, default='')),
                ('Comment', models.CharField(max_length=200, default='')),
                ('Rating', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('SeriesNumber', models.CharField(max_length=200)),
                ('SeriesInstanceUID', models.CharField(max_length=200)),
                ('ProtocolName', models.CharField(max_length=200)),
                ('Modality', models.CharField(max_length=200)),
                ('SeriesDescription', models.CharField(max_length=200, default='')),
                ('SeriesTime', models.CharField(max_length=200, default='')),
                ('ContrastAgent', models.CharField(max_length=200, default='')),
                ('ScanningSequence', models.CharField(max_length=200, default='')),
                ('BodyPartExaminated', models.CharField(max_length=200, default='')),
                ('AcquisitionNumber', models.CharField(max_length=200, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MR_Params',
            fields=[
                ('PixelSpacing', models.CharField(max_length=200, default='')),
                ('SliceThickness', models.CharField(max_length=200, default='')),
                ('EchoTime', models.CharField(max_length=200, default='')),
                ('EchoNumbers', models.CharField(max_length=200, default='')),
                ('InversionTime', models.CharField(max_length=200, default='')),
                ('RepetitionTime', models.CharField(max_length=200, default='')),
                ('modality_params', models.OneToOneField(primary_key=True, serialize=False, to='data_base.Series')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CT_Params',
            fields=[
                ('Name', models.CharField(max_length=200, default='')),
                ('modality_params', models.OneToOneField(primary_key=True, serialize=False, to='data_base.Series')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('StudyDescription', models.CharField(max_length=200)),
                ('StationName', models.CharField(max_length=200)),
                ('ManufacturerModelName', models.CharField(max_length=200)),
                ('StudyInstanceUID', models.CharField(max_length=200)),
                ('Pathology', models.CharField(max_length=200, default='')),
                ('StudyDate', models.CharField(max_length=200, default='')),
                ('StudyTime', models.CharField(max_length=200, default='')),
                ('AccessionNumber', models.CharField(max_length=200, default='')),
                ('InstitutionName', models.CharField(max_length=200, default='')),
                ('ReferringPhysicianName', models.CharField(max_length=200, default='')),
                ('PerformingPhysicianName', models.CharField(max_length=200, default='')),
                ('ModalitiesInStudy', models.CharField(max_length=200, default='')),
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
                ('Name', models.CharField(max_length=200, default='')),
                ('modality_params', models.OneToOneField(primary_key=True, serialize=False, to='data_base.Series')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('UserName', models.CharField(max_length=200, default='')),
                ('RealName', models.CharField(max_length=200, default='')),
                ('UserID', models.CharField(max_length=200, default='')),
                ('Email', models.EmailField(max_length=200, default='')),
                ('group', models.ManyToManyField(to='data_base.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='series',
            name='group',
            field=models.ManyToManyField(to='data_base.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='study',
            field=models.ForeignKey(to='data_base.Study'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='user',
            field=models.ManyToManyField(to='data_base.User'),
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
