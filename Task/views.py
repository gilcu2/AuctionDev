from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from Task.models import *


class IndexView(generic.ListView):
    template_name = 'Task/index.html'
    context_object_name = 'latest_tasks'

    def get_queryset(self):
        """Return the last five published polls."""
        return Task.objects.order_by('-initialDate')[:5]

class DetailView(generic.DetailView):
    model = Task
    template_name = 'Task/detail.html'

class ResultsView(generic.DetailView):
    model = Task
    template_name = 'Task/results.html'

def set_select_proposal(request, task_id):
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