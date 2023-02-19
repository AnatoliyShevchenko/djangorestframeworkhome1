from rest_framework import serializers

from django.db.models import QuerySet

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    """Car Serializer."""

    id = serializers.IntegerField()
    mark = serializers.CharField()
    model = serializers.CharField()
    color = serializers.CharField()
    year_of_issue = serializers.IntegerField()

    class Meta:
        model = Car
        fields = '__all__'