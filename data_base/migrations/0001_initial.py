# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('data_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now=True)),
                ('nb_files', models.BigIntegerField(max_length=20)),
                ('status', models.BigIntegerField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('feed_name', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now=True)),
                ('progress', models.IntegerField()),
                ('duration', models.BigIntegerField(max_length=20)),
                ('visible', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('group_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('patient_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('pathology', models.CharField(max_length=200)),
                ('mrn', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('reviews_name', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=200)),
                ('data', models.ForeignKey(to='data_base.Data')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('series_name', models.CharField(max_length=200)),
                ('data', models.OneToOneField(to='data_base.Data')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('study_name', models.CharField(max_length=200)),
                ('series_name', models.CharField(max_length=200)),
                ('protocol_name', models.CharField(max_length=200)),
                ('station_name', models.CharField(max_length=200)),
                ('manufacturer_name', models.CharField(max_length=200)),
                ('body_part_name', models.CharField(max_length=200)),
                ('slice_thickness', models.IntegerField()),
                ('echo_time', models.FloatField()),
                ('magnetic_field_strenght', models.IntegerField()),
                ('inversion_time', models.IntegerField()),
                ('patient', models.ForeignKey(to='data_base.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tag_name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('membership', models.ManyToManyField(to='data_base.Group')),
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
            model_name='feed',
            name='tag',
            field=models.ManyToManyField(to='data_base.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(to='data_base.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='feed',
            field=models.ManyToManyField(to='data_base.Feed'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='patient',
            field=models.ForeignKey(to='data_base.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='study',
            field=models.ForeignKey(to='data_base.Study'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='user',
            field=models.ManyToManyField(to='data_base.User'),
            preserve_default=True,
        ),
    ]
