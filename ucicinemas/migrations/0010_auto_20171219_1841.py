# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucicinemas', '0009_movie_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='image',
            new_name='picture',
        ),
    ]
