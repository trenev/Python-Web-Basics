from django.urls import path

from django101.tasks.views import home

urlpatterns = (
    path('', home),
)
