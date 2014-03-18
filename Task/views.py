from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from Task.models import *


def index(request):
    latest_tasks = Task.objects.order_by('-initialDate')[:5]
    context = {'latest_tasks': latest_tasks}
    return render(request,'Task/index.html',context)

def detail(request, task_id):
    task=get_object_or_404(Task,pk=task_id)
    return render(request, 'Task/detail.html', {'task': task})


def tests(request, task_id):
    return HttpResponse("You're looking at the test of task %s." % task_id)

def proposals(request, task_id):
    return HttpResponse("You're looking on proposals of task %s." % task_id)