from django.contrib import admin
from .models import Picture, Place
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableTabularInline


class ModelInline(SortableTabularInline):
    model = Picture
    readonly_fields = ('preview_image',)
    fields = ('image', 'preview_image', 'sequence_number',)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" />', obj.image.url)
        return "Добавьте картинку, для отображения превью"

    preview_image.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    inlines = [
        ModelInline,
    ]


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
