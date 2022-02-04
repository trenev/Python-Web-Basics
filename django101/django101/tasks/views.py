from django.shortcuts import render

# Create your views here.
# from django101.tasks.models import Task


def home(request):
    context = {
        'title': 'Tasks manager',
        # 'tasks': Task.objects.all(),
    }

    return render(request, 'home.html', context)
