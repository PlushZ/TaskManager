from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'date', 'status', 'date_end')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'task')
    list_editable = ('status',)
    list_filter=('status', 'date_end')


admin.site.register(Task, TaskAdmin)
