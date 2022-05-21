from django.contrib import admin
from .models import Link, Visitor


class VisitorInline(admin.TabularInline):
    model = Visitor
    verbose_name = 'Latest Visitor'
    max_num = 10
    ordering = ['-visited_at']
    readonly_fields = ['visited_at']
    extra = 0


@admin.register(Link)
class LinkAdminPage(admin.ModelAdmin):
    list_display = ['origin', 'slug', 'created_at']
    search_fields = ['origin', 'slug', 'secret_slug']
    list_filter = ['updated_at', 'created_at', 'is_enabled']
    readonly_fields = ['updated_at', 'created_at']
    inlines = [VisitorInline]


@admin.register(Visitor)
class ViewAdminPage(admin.ModelAdmin):
    list_select_related = ['link']
    list_display = ['origin', 'slug', 'ip']
    search_fields = ['link__origin', 'link__slug', 'ip']
    search_fields = ['visited_at']
    readonly_fields = ['visited_at']

    def origin(self, Visitor):
        return Visitor.link.origin
    
    def slug(self, Visitor):
        return Visitor.link.slug