from django.contrib import admin
from .models import Photography


class PhotographyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subtitle', 'category', 'image', 'published', 'created_at', 'updated_at')
    list_display_links = ('id', 'name', 'subtitle', 'image')
    search_fields = ('name', 'category', 'subtitle', 'description', 'image', 'published', 'created_at', 'updated_at')
    list_filter = ('category', 'published', 'created_at', 'updated_at')
    list_editable = ('published',)
    list_per_page = 10


admin.site.register(Photography, PhotographyAdmin)
