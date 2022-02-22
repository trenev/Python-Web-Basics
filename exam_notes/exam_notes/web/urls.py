from django.urls import path

from exam_notes.web.views import show_home, create_profile, profile_details, add_note, edit_note, delete_note, \
    note_details, delete_profile

urlpatterns = (
    path('', show_home, name='index'),
    path('create/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/', profile_details, name='profile details'),

    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', note_details, name='note details'),

)
