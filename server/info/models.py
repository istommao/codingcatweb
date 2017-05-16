"""info models."""
from django.db import models

from extensions.modelutils import RandomFixedCharField


class Article(models.Model):
    """Article Model."""

    uid = RandomFixedCharField('编号', max_length=16, unique=True)

    title = models.CharField('标题', max_length=32)
    intro = models.CharField('简介', max_length=128, default='')

    creation_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        """Article Meta."""
        verbose_name = '文章管理'
        verbose_name_plural = '文章管理'
