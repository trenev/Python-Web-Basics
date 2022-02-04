from django.contrib import admin

# Register your models here.
from task_manager.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'dead_line', 'status')
    list_filter = ('title',)
