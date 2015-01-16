# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(db_index=True, unique=True, max_length=255, validators=[django.core.validators.MaxLengthValidator(255)])),
                ('slug', models.SlugField(unique=True, max_length=255, validators=[django.core.validators.MaxLengthValidator(255)])),
                ('body', models.TextField()),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'db_table': 'blog',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100, validators=[django.core.validators.MaxLengthValidator(255)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog_app.Tags', verbose_name=b'blog_tags'),
            preserve_default=True,
        ),
    ]
