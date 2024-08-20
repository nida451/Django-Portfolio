from django.contrib import admin
from .models import Post

@admin.register(Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'content')
    search_fields = ('title', 'content')
    list_filter = ('author', 'title')
#    ordering = ('-created_at',)

admin.site.site_header = "My API Admin"
admin.site.site_title = "My API"
admin.site.index_title = "Welcome to My API"
