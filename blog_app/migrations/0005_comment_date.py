# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 1, 53, 21, 529721, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
