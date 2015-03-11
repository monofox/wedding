# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('wishcover', models.ImageField(upload_to='upload/wishes')),
                ('wishtxt', models.TextField()),
                ('wishisbn', models.CharField(max_length=120)),
                ('visible', models.BooleanField(default=False)),
                ('dtticrt', models.DateTimeField(auto_now_add=True)),
                ('dttichg', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Wish',
                'ordering': ['priority'],
                'verbose_name_plural': 'Wishes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WishPriority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('weight', models.PositiveSmallIntegerField()),
                ('priotxt', models.CharField(max_length=125)),
            ],
            options={
                'verbose_name': 'Wish Priority',
                'ordering': ['weight'],
                'verbose_name_plural': 'Wish Priorities',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='wish',
            name='priority',
            field=models.ForeignKey(to='wishes.WishPriority'),
            preserve_default=True,
        ),
    ]
