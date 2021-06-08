from django.contrib import admin
from .models import Adver, Owner, Type, Status


@admin.register(Adver)
class AdverAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'upd_time', 'description']
    list_filter = ['title', 'upd_time', 'description']
    search_fields = ['title', 'description']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
