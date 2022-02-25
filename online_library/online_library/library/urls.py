from django.urls import path

from online_library.library.views import show_home, add_book, edit_book, book_details, create_profile, edit_profile, \
    delete_profile, show_profile, delete_book

urlpatterns = (
    path('', show_home, name='index'),

    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('details/<int:pk>/', book_details, name='book details'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/', show_profile, name='show profile'),
)
