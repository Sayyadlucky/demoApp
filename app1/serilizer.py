from rest_framework import serializers
from .models import StudInfo


class StudSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudInfo
        fields = '__all__'
