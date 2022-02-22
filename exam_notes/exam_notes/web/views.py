from django.shortcuts import render, redirect

from exam_notes.web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from exam_notes.web.helpers import get_profile, get_notes
from exam_notes.web.models import Note


def show_home(request):
    profile = get_profile()
    notes = get_notes()
    print(request.path)
    if not profile:
        return redirect('create profile')
    else:
        context = {
            'notes': notes,
            # 'path': request.get_full_path(),
        }

        return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    content = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', content)


def delete_profile(request):
    profile = get_profile()
    notes = get_notes()
    if notes:
        notes.delete()
    profile.delete()

    return redirect('index')


def profile_details(request):
    profile = get_profile()
    notes_count = get_notes().count()

    context = {
        'profile': profile,
        'notes_count': notes_count,
    }
    return render(request, 'profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)

