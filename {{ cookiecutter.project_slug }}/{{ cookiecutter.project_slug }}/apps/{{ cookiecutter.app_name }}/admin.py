from django.contrib import admin

from {{ cookiecutter.project_slug }}.apps.{{ cookiecutter.app_name }}.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
