# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucicinemas', '0008_remove_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
