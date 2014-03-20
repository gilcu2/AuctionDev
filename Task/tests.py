from django.test import TestCase



from Task.models import *

class TaskMethodTests(TestCase):

    def test_proper_subtask(self):
        """
        A task can't be subtask of inself
        """
        user=User(name='testuser')
        user.save()
        task=Task(owner=user, initialCost=1, initialDuration=1)
        task.save()
        task.subtasks.add(task)
        for ta in task.subtasks.all():
            self.assertEqual(task==ta, False)
