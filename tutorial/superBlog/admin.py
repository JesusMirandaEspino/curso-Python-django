from django.contrib import admin
from .models import Post


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('title', 'created', 'modified')
    date_hierarchy = 'created'  # nuevo

admin.site.register(Post, PostAdmin)
