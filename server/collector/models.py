"""collector models."""
from django.db import models

from extensions.modelutils import RandomFixedCharField, PathAndRename

from collector import consts


class ResourceType(models.Model):
    """资源类型."""

    uid = RandomFixedCharField('编号', max_length=6, unique=True)

    name = models.CharField('名称', max_length=32)

    creation_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        """Meta."""
        verbose_name = '资源类型'
        verbose_name_plural = '资源类型'


class Resource(models.Model):
    """资源."""

    uid = RandomFixedCharField('编号', max_length=16, unique=True)
    title = models.CharField('标题', max_length=32)
    intro = models.CharField('简介', max_length=100)
    link = models.URLField('链接', max_length=200, default='')

    image = models.ImageField(
        '图片', upload_to=PathAndRename('collector/'),
        default=consts.DEFAULT_IMAGE
    )

    category = models.ForeignKey('collector.ResourceType', verbose_name='类型',
                                 related_name='resources')

    creation_time = models.DateTimeField('创建时间', auto_now_add=True)
    updation_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        """Meta."""
        verbose_name = '资源管理'
        verbose_name_plural = '资源管理'
