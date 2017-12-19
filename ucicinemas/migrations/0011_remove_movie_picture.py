# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucicinemas', '0010_auto_20171219_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='picture',
        ),
    ]
