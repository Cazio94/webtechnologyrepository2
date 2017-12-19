# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucicinemas', '0013_auto_20171219_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
