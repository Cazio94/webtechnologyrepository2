# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucicinemas', '0007_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='image',
        ),
    ]
