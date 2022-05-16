from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here.

# class itemInLine(admin.StackedInline):
#     model = item
#     extra = 1

# class ContainerAdmin(admin.ModelAdmin):
#     inlines = [itemInLine]



admin.site.register(season)
admin.site.register(container)
admin.site.register(item)
admin.site.register(item_container)

# admin.site.register(container, ContainerAdmin)