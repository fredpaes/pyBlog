from django.contrib import admin
from app_one.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('title', 'created', 'slug')
    search_fields = ('title', 'slug', 'body')
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, PostAdmin)
