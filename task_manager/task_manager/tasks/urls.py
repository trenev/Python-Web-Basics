from django.urls import path

from task_manager.tasks.views import show_home, delete_task, start_task, finish_task

urlpatterns = (
    path('', show_home, name='index'),
    path('delete/<int:pk>/', delete_task, name='delete task'),
    path('start/<int:pk>/', start_task, name='start task'),
    path('finish/<int:pk>/', finish_task, name='finish task'),
)
