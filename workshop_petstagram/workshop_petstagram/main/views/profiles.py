from django.shortcuts import render, redirect

from workshop_petstagram.main.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from workshop_petstagram.main.helpers import get_profile
from workshop_petstagram.main.models import Pet, PetPhoto, Profile
from workshop_petstagram.main.templatetags.profiles import has_profile


def show_profile(request):
    if not has_profile():
        return redirect('error page')

    profile = get_profile()
    pets = list(Pet.objects.filter(user_profile=profile))

    pet_photos = PetPhoto.objects\
        .filter(tagged_pets__in=pets)\
        .distinct()

    total_likes_count = sum(photo.likes for photo in pet_photos)
    total_pet_photos_count = len(pet_photos)

    context = {
        'profile': profile,
        'pets': pets,
        'total_likes_count': total_likes_count,
        'total_pet_photos_count': total_pet_photos_count,
    }
    return render(request, 'profile_details.html', context)


def profile_action(request, form_class, success_url, instance, template_name):
    if not has_profile():
        return redirect('error page')

    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
    }

    return render(request, template_name, context)


def create_profile(request):
    return profile_action(request, CreateProfileForm, 'index', Profile(), 'profile_create.html')


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'profile', get_profile(), 'profile_edit.html')


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'profile_delete.html')
