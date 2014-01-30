# coding: utf8

from django.contrib import admin
from .models import Project

admin.site.register(Client)


class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('name', 'completion_date', 'client', 'in_development', 'is_public')
    list_filter   = ('in_development', 'is_public')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin)