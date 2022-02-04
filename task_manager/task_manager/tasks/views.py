from django.http import HttpResponse
from django.shortcuts import render
from task_manager.tasks.models import Task

# Create your views here.


# def home(request):
#     html = f'''
#     <h1>Hello</h1>'''
#     return HttpResponse(html)


def home(request):
    context = {
        'open': list(Task.objects.filter(status__exact=1)),
        'in_progress': list(Task.objects.filter(status__exact=2)),
        'complete': list(Task.objects.filter(status__exact=3)),
    }

    return render(request, 'index.html', context)
