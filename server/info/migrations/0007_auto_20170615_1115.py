# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 11:15
from __future__ import unicode_literals

from django.db import migrations
import simditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20170615_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=simditor.fields.RichTextField(default='', verbose_name='内容'),
        ),
    ]
