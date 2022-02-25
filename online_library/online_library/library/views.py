from django.shortcuts import render, redirect

from online_library.library.forms import CreateProfileForm, CreateBookForm, EditBookForm, EditProfileForm, \
    DeleteProfileForm
from online_library.library.helpers import get_profile
from online_library.library.models import Book


def show_home(request):
    profile = get_profile()
    al_books = Book.objects.all()
    books_list = []
    row = []

    for i in range(len(Book.objects.all())):
        row.append(al_books[i])
        if (i + 1) % 3 == 0:
            books_list.append(row)
            row = []

    if len(row) > 0:
        books_list.append(row)

    context = {
        'books': books_list,
    }

    if profile:
        return render(request, 'home-with-profile.html', context)
    else:
        return redirect('create profile')


def add_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateBookForm()

    context = {
        'form': form,
    }

    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditBookForm(instance=book)

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('index')


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }

    return render(request, 'book-details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)


