from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

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

def select_proposal(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    try:
        selected_proposal = task.proposals.get(pk=request.POST['proposal'])
    except (KeyError, Proposal.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'Task/detail.html', {
            'task': task,
            'error_message': "proposal don't exist",
        })
    else:

        task.selectedProposal=selected_proposal
        task.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('task:results', args=(task.id,)))

def results(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'Task/results.html', {'task': task})