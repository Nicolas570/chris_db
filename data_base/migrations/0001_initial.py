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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=200)),
                ('Time', models.DateTimeField(auto_now=True)),
                ('NbFiles', models.BigIntegerField()),
                ('Progress', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('Time', models.DateTimeField(auto_now=True)),
                ('Status', models.FloatField()),
                ('Duration', models.BigIntegerField()),
                ('Visible', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MR_Params',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('SliceThickness', models.IntegerField(default=0)),
                ('EchoTime', models.FloatField(default=0)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('PatientName', models.CharField(max_length=200)),
                ('PatientSex', models.CharField(max_length=200)),
                ('PatientBirthdate', models.DateField()),
                ('PatientAge', models.IntegerField(default=0)),
                ('PatientId', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('Comment', models.CharField(max_length=200)),
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
                ('Name', models.CharField(max_length=200)),
                ('SeriesName', models.CharField(max_length=200)),
                ('SeriesInstanceUID', models.CharField(max_length=200)),
                ('ProtocolName', models.CharField(max_length=200)),
                ('data', models.OneToOneField(to='db.Data')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('Pathology', models.CharField(max_length=200)),
                ('StationName', models.CharField(max_length=200)),
                ('ManufacturerModelName', models.CharField(max_length=200)),
                ('BodyPartExaminated', models.CharField(max_length=200)),
                ('MagneticFieldStrength', models.IntegerField(default=0)),
                ('Modality', models.CharField(max_length=200)),
                ('StudyInstanceUID', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(to='db.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('Color', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Value', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='US_Params',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('modality_params', models.OneToOneField(to='db.Series')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=200)),
                ('group', models.ManyToManyField(to='db.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='series',
            name='study',
            field=models.ForeignKey(to='db.Study'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='study',
            field=models.ForeignKey(to='db.Study'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mr_params',
            name='modality_params',
            field=models.OneToOneField(to='db.Series'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feed',
            name='tag',
            field=models.ManyToManyField(to='db.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(to='db.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='feed',
            field=models.ManyToManyField(to='db.Feed'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='patient',
            field=models.ForeignKey(to='db.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='study',
            field=models.ForeignKey(to='db.Study'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='user',
            field=models.ManyToManyField(to='db.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ct_params',
            name='modality_params',
            field=models.OneToOneField(to='db.Series'),
            preserve_default=True,
        ),
    ]
