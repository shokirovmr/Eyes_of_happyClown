from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.keylogger.views import KeyLoggerViewsets

router = DefaultRouter()
router.register(r"logs", KeyLoggerViewsets)


urlpatterns = [
    path("", include(router.urls)),
]