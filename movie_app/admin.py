from django.contrib import admin
from django.utils.html import format_html
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_year", "is_new", "image_preview")
    list_editable = ("is_new",)
    list_display_links = ("title",)
    search_fields = ("title", "description")
    list_filter = ("release_year", "is_new")
    list_per_page = 10

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" '
                'style="object-fit: cover; border-radius: 8px;" />',
                obj.image.url
            )
        return "(Aucune image)"

    image_preview.short_description = "Aperçu de l'image"
