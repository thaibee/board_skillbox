from django.contrib import admin
from .models import Adver, Owner, Type, Status


@admin.register(Adver)
class AdverAdmin(admin.ModelAdmin):
    pass


@admin.register(Owner)
class AdverAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
