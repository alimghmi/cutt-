from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdminPage(admin.ModelAdmin):
    list_display = ['origin', 'slug', 'created_at']
    search_fields = ['origin', 'slug', 'delete_slug']
    list_filter = ['updated_at', 'created_at', 'is_enabled']
    readonly_fields = ['updated_at', 'created_at']

