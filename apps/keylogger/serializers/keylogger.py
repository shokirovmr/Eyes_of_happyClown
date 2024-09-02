from rest_framework import serializers
from apps.keylogger.models import KeyLogger


class KeyLoggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyLogger
        fields = '__all__'
