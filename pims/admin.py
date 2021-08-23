from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here.


class containerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['']})
    ]

admin.site.register(season)
admin.site.register(container)
admin.site.register(item)