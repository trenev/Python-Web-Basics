from django.urls import path

from furniture_store.web.views import show_home, create_user, login_user, edit_user, logout_user, \
    show_my_publications, create_furniture, edit_furniture, delete_furniture, furniture_details

urlpatterns = (
    path('', show_home, name='index'),

    path('register/', create_user, name='create user'),
    path('login/', login_user, name='login user'),
    path('edit/', edit_user, name='edit user'),
    path('logout/', logout_user, name='logout user'),

    path('data/publications/', show_my_publications, name='show my publications'),
    path('data/create/', create_furniture, name='create furniture'),
    path('data/edit/<int:pk>/', edit_furniture, name='edit furniture'),
    path('data/delete/<int:pk>/', delete_furniture, name='delete furniture'),
    path('data/details/<int:pk>/', furniture_details, name='furniture details'),
)
