# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='dttiord',
            field=models.DateTimeField(null=True, default=None),
            preserve_default=True,
        ),
    ]
