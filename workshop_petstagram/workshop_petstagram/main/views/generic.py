from django.shortcuts import render

from workshop_petstagram.main.helpers import get_profile
from workshop_petstagram.main.models import PetPhoto


def show_home(request):
    context = {
        'hide_additional_buttons': True,
    }

    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pet_photos = PetPhoto.objects\
        .prefetch_related('tagged_pets')\
        .filter(tagged_pets__user_profile=profile)\
        .distinct()

    context = {
        'pet_photos': pet_photos,
    }

    return render(request, 'dashboard.html', context)
