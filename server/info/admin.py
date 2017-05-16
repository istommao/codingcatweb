"""info admin."""
from django.contrib import admin

from info.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """ArticleAdmin."""

    list_display = ('uid', 'title', 'creation_time')

    search_fields = ('title', 'uid')
