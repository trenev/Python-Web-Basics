from django.urls import path

from task_manager.tasks.views import home

urlpatterns = (
    path('', home),
)
