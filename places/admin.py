from django.contrib import admin
from .models import Picture, Place


class ModelInline(admin.TabularInline):
    model = Picture


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ModelInline,
    ]


admin.site.register(Picture)
