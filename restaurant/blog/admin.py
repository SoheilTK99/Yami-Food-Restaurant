from django.contrib import admin
from .models import Blog , Category , Tag , Comments

# admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments)


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","created_at","author")
    search_fields = ("title",)
    ordering = ("created_at",)
admin.site.register(Blog,BlogAdmin)