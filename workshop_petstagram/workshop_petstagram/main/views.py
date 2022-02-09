from django.shortcuts import render

from workshop_petstagram.main.models import Profile, PetPhoto, Pet


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None


def show_home(request):
    context = {
        'hide_additional_buttons': True,
    }

    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pet_photos = set(PetPhoto.objects
                     .prefetch_related('tagged_pets')
                     .filter(tagged_pets__user_profile=profile))

    context = {
        'pet_photos': pet_photos,
    }

    return render(request, 'dashboard.html', context)


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects \
        .prefetch_related('user_profile') \
        .filter(user_profile=profile)

    pet_photos = set(PetPhoto.objects
                     .prefetch_related('tagged_pets')
                     .filter(tagged_pets__user_profile=profile))

    context = {
        'profile': profile,
        'total_images': len(pet_photos),
        'pets': pets,
    }
    return render(request, 'profile_details.html', context)


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects \
        .prefetch_related('tagged_pets') \
        .get(pk=pk)

    context = {
        'pet_photo': pet_photo
    }

    return render(request, 'photo_details.html', context)
