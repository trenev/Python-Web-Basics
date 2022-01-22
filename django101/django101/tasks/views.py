from django.http import HttpResponse
from django.shortcuts import render
from django101.tasks.models import Task

# Create your views here.


# def home(request):
#     html = f'''
#     <h1>Hello</h1>
#     '''
#     return HttpResponse(html)


def home(request):
    context = {
        'title': 'Tasks manager',
        'tasks': Task.objects.all(),
    }

    return render(request, 'home.html', context)
