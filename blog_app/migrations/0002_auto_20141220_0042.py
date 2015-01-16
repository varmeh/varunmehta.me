# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='slug',
            field=models.SlugField(max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+$'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid'), django.core.validators.MaxLengthValidator(255)]),
            preserve_default=True,
        ),
    ]
