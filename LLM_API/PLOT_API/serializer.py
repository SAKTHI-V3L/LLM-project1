# serializers.py
from rest_framework import serializers

class PlotRequestSerializer(serializers.Serializer):
    get_what_need = serializers.IntegerField()
    headline_1 = serializers.CharField(required=False, allow_blank=True)
    headline_2 = serializers.CharField(required=False, allow_blank=True)
    headline_3 = serializers.CharField(required=False, allow_blank=True)
