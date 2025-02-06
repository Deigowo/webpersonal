from django.contrib import admin

# Register your models here.
from .models import Project

# admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']