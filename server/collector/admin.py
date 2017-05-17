"""collector admin."""

from django.contrib import admin

from collector.models import Resource, ResourceType


@admin.register(ResourceType)
class ResourceTypeAdmin(admin.ModelAdmin):
    """ResourceTypeAdmin."""

    list_display = ('uid', 'name', 'creation_time')

    search_fields = ('name',)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    """ResourceAdmin."""

    list_display = ('uid', 'title', 'creation_time')

    search_fields = ('title', 'uid')
