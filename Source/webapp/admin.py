from django.contrib import admin

from webapp.models import ToDoList


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'detailed_description', 'status', 'created_at']
    list_display_links = ['id', 'description']
    list_filter = ['status']
    search_fields = ['title', 'description']
    fields = ['description', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(ToDoList, ToDoListAdmin)
