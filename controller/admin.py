from django.contrib import admin
from .models import SonosBox, MusicCategory, MusicItem


class SonosBoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'volume_max')
    prepopulated_fields = {"slug": ("name",)}


class MusicCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'get_child_count')


class MusicItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'episode_no', 'category')


admin.site.register(SonosBox, SonosBoxAdmin)
admin.site.register(MusicCategory, MusicCategoryAdmin)
admin.site.register(MusicItem, MusicItemAdmin)
