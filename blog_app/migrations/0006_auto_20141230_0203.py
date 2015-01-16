# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_comment_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-published_on']},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='modified',
            new_name='modified_on',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='created',
            new_name='published_on',
        ),
    ]
