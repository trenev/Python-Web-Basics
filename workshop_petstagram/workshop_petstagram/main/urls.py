from django.urls import path

from workshop_petstagram.main.views.generic import show_home, show_dashboard, show_error_page
from workshop_petstagram.main.views.pet_photos import show_pet_photo_details, add_pet_photo, edit_pet_photo, \
    like_pet_photo, delete_pet_photo
from workshop_petstagram.main.views.pets import add_pet, edit_pet, delete_pet
from workshop_petstagram.main.views.profiles import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('error/', show_error_page, name='error page'),

    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('pet/add/', add_pet, name='add pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),

    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/add/', add_pet_photo, name='add pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/delete/<int:pk>/', delete_pet_photo, name='delete pet photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
)
