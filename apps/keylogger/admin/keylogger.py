from django.contrib import admin
from apps.keylogger.models import KeyLogger

@admin.register(KeyLogger)
class KeyloggerAdmin(admin.ModelAdmin):
    list_display = ['logs']