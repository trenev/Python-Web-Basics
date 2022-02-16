from django.shortcuts import render, redirect

from workshop_petstagram.main.helpers import get_profile_pet_photos
from workshop_petstagram.main.templatetags.profiles import has_profile


def show_home(request):
    context = {
        'hide_additional_buttons': True,
    }

    return render(request, 'home_page.html', context)


def show_dashboard(request):
    if not has_profile():
        return redirect('error page')

    pet_photos = get_profile_pet_photos()

    context = {
        'pet_photos': pet_photos,
    }

    return render(request, 'dashboard.html', context)


def show_error_page(request):
    return render(request, '401_error.html')
