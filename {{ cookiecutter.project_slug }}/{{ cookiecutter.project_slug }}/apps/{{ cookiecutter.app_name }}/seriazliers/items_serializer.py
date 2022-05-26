from rest_framework import serializers

from {{ cookiecutter.project_slug }}.apps.{{ cookiecutter.app_name }}.models import Item


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ("id",)
