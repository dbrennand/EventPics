from django.contrib import admin
from .models import Gallery, Photo

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    filter_horizontal = ('allowed_users',)

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo)
