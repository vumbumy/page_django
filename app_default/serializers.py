from rest_framework import serializers

from app_default.models import Project


class DefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
