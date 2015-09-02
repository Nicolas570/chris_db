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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Value', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=200)),
                ('group', models.ManyToManyField(to='UsrDb.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='feed',
            name='tag',
            field=models.ManyToManyField(to='UsrDb.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(to='UsrDb.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='feed',
            field=models.ManyToManyField(to='UsrDb.Feed'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='user',
            field=models.ManyToManyField(to='UsrDb.User'),
            preserve_default=True,
        ),
    ]
