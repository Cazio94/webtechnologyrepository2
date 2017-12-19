# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucicinemas', '0011_remove_movie_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='main_image',
            field=models.URLField(default='https://www.youtube.com/embed/dX3k_QDnzHE'),
            preserve_default=False,
        ),
    ]
