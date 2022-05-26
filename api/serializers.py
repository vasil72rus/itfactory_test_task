from rest_framework import serializers
from .models import Worker, SalesPoint, Visiting


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('name', 'phone')


class SalesPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPoint
        fields = ('pk', 'name')


class VisitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visiting
        fields = ('sales_point', 'latitude', 'longitude')