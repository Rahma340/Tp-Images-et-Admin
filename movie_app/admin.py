from django.contrib import admin
from .models import Movie

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title" , "release_year" , "is_new",)

    list_editable = ("is_new",)

    list_display_links = ("title",)

    search_fields = ("title" , "description",)