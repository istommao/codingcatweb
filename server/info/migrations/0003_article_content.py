# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 09:48
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_article_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(default='', verbose_name='内容'),
        ),
    ]
