from django.shortcuts import render, redirect

from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task


def show_home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    context = {
        'open': Task.objects.filter(status__exact='Open'),
        'in_progress': Task.objects.filter(status__exact='In progress'),
        'complete': Task.objects.filter(status__exact='Complete'),
        'form': form,
    }

    return render(request, 'index.html', context)


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('index')


def start_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = 'In progress'
    task.save()
    return redirect('index')


def finish_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = 'Complete'
    task.save()
    return redirect('index')
