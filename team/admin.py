from django.contrib import admin
from team.models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','designation','profile_image')
    list_filter = ('designation',)

admin.site.register(Team,TeamAdmin)