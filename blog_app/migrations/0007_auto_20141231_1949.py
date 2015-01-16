# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20141230_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_on',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
