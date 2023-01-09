from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here

class ContainerAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("location","row_letter","column_number")}

class SeasonAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(season, SeasonAdmin)
admin.site.register(container, ContainerAdmin)
admin.site.register(item, ItemAdmin)
admin.site.register(item_container)

# admin.site.register(container, ContainerAdmin)