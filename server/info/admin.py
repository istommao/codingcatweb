"""info admin."""
from django import forms
from django.contrib import admin

from info.models import Article, News

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class InfoAdminForm(forms.ModelForm):
    content = forms.CharField(label='内容', widget=CKEditorUploadingWidget())


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """ArticleAdmin."""

    form = InfoAdminForm

    list_display = ('uid', 'title', 'creation_time')

    search_fields = ('title', 'uid')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """NewsAdmin."""

    list_display = ('uid', 'title', 'creation_time')

    search_fields = ('title', 'uid')
