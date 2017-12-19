# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ucicinemas', '0006_remove_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.URLField(default=datetime.datetime(2017, 12, 19, 17, 23, 4, 151691, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
