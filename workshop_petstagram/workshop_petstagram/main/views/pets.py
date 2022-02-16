from django.shortcuts import render, redirect

from workshop_petstagram.main.forms import AddPetForm, EditPetForm, DeletePetForm
from workshop_petstagram.main.helpers import get_profile
from workshop_petstagram.main.models import Pet
from workshop_petstagram.main.templatetags.profiles import has_profile


def pet_action(request, form_class, success_url, instance, template_name):
    if not has_profile():
        return redirect('error page')

    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    content = {
        'form': form,
        'pet': instance,
    }

    return render(request, template_name, content)


def add_pet(request):
    return pet_action(request, AddPetForm, 'profile', Pet(user_profile=get_profile()), 'pet_create.html')


def edit_pet(request, pk):
    return pet_action(request, EditPetForm, 'profile', Pet.objects.get(pk=pk), 'pet_edit.html')


def delete_pet(request, pk):
    return pet_action(request, DeletePetForm, 'profile', Pet.objects.get(pk=pk), 'pet_delete.html')
