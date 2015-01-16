# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20141220_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(max_length=255)),
                ('comment_on', models.ForeignKey(verbose_name=b'comment_on_blog', to='blog_app.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
