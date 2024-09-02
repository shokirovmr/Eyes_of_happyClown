from django.db import models
from apps.shared.models import AbstractBaseModel


class KeyLogger(AbstractBaseModel):
    logs = models.TextField(null=True, blank=True)
