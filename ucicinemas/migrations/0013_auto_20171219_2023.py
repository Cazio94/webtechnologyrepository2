# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ucicinemas', '0012_movie_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='late_show',
            field=models.CharField(default=22.45, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='onScreen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='prime_time',
            field=models.CharField(default=20.45, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='room',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
