# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-07-14 21:11
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('profiles', '0004_auto_20180714_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='expertise',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
