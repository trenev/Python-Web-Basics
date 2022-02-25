from django.shortcuts import render, redirect

from furniture_store.web.forms import CreateFurnitureForm, EditFurnitureForm
from furniture_store.web.models import Furniture


def create_user(request):
    return render(request, 'register.html')


def login_user(request):
    return render(request, 'login.html')


def edit_user(request):
    return render(request, 'login.html')


def logout_user(request):
    return render(request, 'login.html')


def show_home(request):
    items = Furniture.objects.all()
    context = {
        'items': items,
    }

    return render(request, 'catalog.html', context)


def show_my_publications(request):
    items = Furniture.objects.filter(user_profile_id=1)
    context = {
        'items': items,
    }

    return render(request, 'my-furniture.html', context)


def create_furniture(request):
    if request.method == 'POST':
        form = CreateFurnitureForm(request.POST)
        if form.is_valid():
            furniture = Furniture(**form.cleaned_data, user_profile_id=1)
            furniture.save()
            return redirect('index')

    else:
        form = CreateFurnitureForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def edit_furniture(request, pk):
    item = Furniture.objects.get(pk=pk)
    initial_dict = {
        'type': item.type,
        'price': item.price,
        'model': item.model,
        'image': item.image,
        'year': item.year,
        'material': item.material,
        'description': item.description,
    }

    if request.method == 'POST':
        form = EditFurnitureForm(request.POST, initial=initial_dict)
        if form.is_valid():
            furniture = Furniture(**form.cleaned_data, user_profile_id=1)
            item.delete()
            furniture.save()
            return redirect('index')
    else:
        form = EditFurnitureForm(initial=initial_dict)

    context = {
        'form': form,
        'item': item,
    }

    return render(request, 'edit.html', context)


def delete_furniture(request, pk):
    item = Furniture.objects.get(pk=pk)
    item.delete()
    return redirect('index')


def furniture_details(request, pk):
    item = Furniture.objects.get(pk=pk)
    context = {
        'item': item,
    }

    return render(request, 'details.html', context)
