from django.urls import path

from my_music_app.web.views import show_home, add_album, edit_album, delete_album, album_details, create_profile, \
    delete_profile, profile_details

urlpatterns = (
    path('', show_home, name='index'),

    path('album/add/', add_album, name='add album'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('album/details/<int:pk>/', album_details, name='album details'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/details/', profile_details, name='profile details'),
)
