# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucicinemas', '0003_auto_20171219_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Director',
            new_name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Movieimage',
        ),
    ]
