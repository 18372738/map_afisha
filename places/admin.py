from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableTabularInline

from .models import Picture, Place


class ModelInline(SortableTabularInline):
    model = Picture
    readonly_fields = ("preview_image",)
    fields = ("image", "preview_image", "sequence_number",)

    def preview_image(self, obj):
        width = 150
        height = 150
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:{}px; max-height:{}px;" />',
                obj.image.url,
                width,
                height,
            )
        return "Добавьте картинку, для отображения превью"

    preview_image.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ("title",)
    inlines = [
        ModelInline,
    ]


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    raw_id_fields = ["place"]
