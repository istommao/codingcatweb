# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import extensions.modelutils


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', extensions.modelutils.RandomFixedCharField(editable=False, max_length=16, unique=True, verbose_name='编号')),
                ('image', models.ImageField(default='info/default.png', upload_to=extensions.modelutils.PathAndRename('news/'), verbose_name='图片')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('intro', models.CharField(default='', max_length=128, verbose_name='简介')),
                ('link', models.URLField(verbose_name='链接')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '新闻管理',
                'verbose_name': '新闻管理',
            },
        ),
    ]