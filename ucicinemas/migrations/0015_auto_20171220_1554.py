# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucicinemas', '0014_auto_20171219_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
