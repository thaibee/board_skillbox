from django.contrib import admin
from .models import Testing


@admin.register(Testing)
class TestingAdmin(admin.ModelAdmin):
    pass
