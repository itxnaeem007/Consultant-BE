from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','short_description','image')
    list_filter = ('name')


admin.site.register(Service)
