from django.db import models
from django.utils import timezone

# A task is any thing to do.
# Must include:
# - owner: Who propouse the task, check and paid
# - maker: Who make the task
# - state: Proposal, asigned, working, testing,done
# - subtasks: Task needed to make this task. A final task(without subtask) must be clear, simple and able to be make by one person.
#   If not, it must be divide by the owner or the maker, into another tasks
# - price: Price proposal by the owner
# - time: Time to done proposal by the owner
# - proposals: proposals of makers to do it
# - tests: its test
# - tags: tags to classify
class Task(models.Model):

    State_Proposal=0
    State_Asigned=1
    State_Working=2
    State_Testing=3
    State_Done=4
    states=((State_Proposal,'Proposal'),
            (State_Asigned,'Asigned'),
            (State_Working,'Working'),
            (State_Testing,'Testing'),
            (State_Done,'Done'))

    title=models.CharField(max_length=50)
    description=models.TextField()
    state=models.IntegerField(choices=states,default=State_Proposal)

    owner=models.ForeignKey('User',related_name='task_owner')
    maker=models.ForeignKey('User',related_name='task_maker', null=True, blank=True)

    subtasks=models.ManyToManyField('self', null=True, blank=True)

    initialCost=models.IntegerField()
    initialDuration=models.IntegerField()
    initialDate=models.DateTimeField(default=timezone.now())

    asignedCost=models.IntegerField(null=True, blank=True)
    assignedDuration=models.IntegerField(null=True, blank=True)
    asignedDate=models.DateTimeField(null=True, blank=True)

    takedTime=models.DateTimeField(null=True, blank=True)

    finalCost=models.IntegerField(null=True, blank=True)
    finalDuration=models.IntegerField(null=True, blank=True)
    finalDate=models.DateTimeField(null=True, blank=True)

    proposals=models.ManyToManyField('Proposal', null=True, blank=True)
    selectedProposal=models.ForeignKey('Proposal', null=True, blank=True))

    tests=models.ManyToManyField('Test', null=True, blank=True)

    tags=models.ManyToManyField('Tag', null=True, blank=True)

    primary=models.BooleanField(default=True)

    priority=models.ForeignKey('Priority', null=True, blank=True)

    def __str__(self):
        return ''.join((self.title,' ',str(self.initialDate),' ',str(self.owner),
                       ' ',str(self.primary),' ',str(self.priority)))

    def left_time(self):
        if self.state==self.State_Proposal:
            return self.initialDuration
        elif self.state==self.State_Asigned:
            return self.assignedDuration
        else:
            return self.assignedDuration-(timezone.now()-self.takedTime)


class User(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):  # Python 3: def __str__(self):
        return self.name

class Proposal(models.Model):
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    time=models.DateTimeField(default=timezone.now())
    chat=models.ForeignKey('Chat',null=True, blank=True)

class Test(models.Model):
    State_ToCheck=0
    State_Failed=1
    State_OK=2
    states={(State_ToCheck,'ToCheck'),
            (State_Failed,'Failed'),
            (State_OK,'OK')}

    title=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    state=models.IntegerField(choices=states,default=State_ToCheck)
    chat=models.ForeignKey('Chat', null=True, blank=True)

    def __str__(self):
        return ''.join(self.title,' ',str(self.state))

class Tag(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    color=models.IntegerField()

    def __str__(self):
        return self.title

class Chat(models.Model):
    entrys=models.ForeignKey('Entry', blank=True,null=True)


class Entry(models.Model):
    text=models.CharField(max_length=500)
    date=models.DateTimeField(default=timezone.now())
    publisher=models.ForeignKey('User',related_name='entry_publisher')

    def __str__(self):
        return ''.join(self.publisher.name,' ',str(self.date))

class Priority(models.Model):
    name=models.CharField(max_length=20)
    priority=models.IntegerField()

    def __str__(self):
        return self.name




