# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('release_date', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
                ('Director', models.CharField(max_length=25)),
                ('trailer', models.URLField()),
                ('poster', models.FileField(upload_to='')),
            ],
        ),
    ]
