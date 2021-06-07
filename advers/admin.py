from django.contrib import admin
from .models import Adver, Owner


@admin.register(Adver)
class AdverAdmin(admin.ModelAdmin):
    pass

@admin.register(Owner)
class AdverAdmin(admin.ModelAdmin):
    pass
