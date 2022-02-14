from django.shortcuts import render, redirect

from workshop_petstagram.main.forms import EditPetPhotoForm, AddPetPhotoForm
from workshop_petstagram.main.models import PetPhoto


def add_pet_photo(request):
    if request.method == "POST":
        form = AddPetPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddPetPhotoForm()

    context = {
        'form': form,
    }

    return render(request, 'photo_create.html', context)


def edit_pet_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetPhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditPetPhotoForm(instance=photo)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photo_edit.html', context)


def delete_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.delete()
    return redirect('dashboard')


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('pet photo details', pk)


def show_pet_photo_details(request, pk):
    pet_photo = PetPhoto.objects \
        .prefetch_related('tagged_pets') \
        .get(pk=pk)

    context = {
        'pet_photo': pet_photo
    }

    return render(request, 'photo_details.html', context)
