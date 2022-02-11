from django.urls import path

from exam_recipes.web.views import show_home, create_recipe, edit_recipe, delete_recipe, \
    show_details_recipe

urlpatterns = (
    path('', show_home, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', show_details_recipe, name='details recipe'),
)
