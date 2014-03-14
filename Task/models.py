from django.db import models

# A task is any thing to do.
# Must include:
# - owner: Who propouse the task, check and paid
# - maker: Who make the task
# - state: Proposal, asigned, working, testing,done
# - subtasks: A final task(without subtask) must be clear, simple and able to be make by one person.
#   If not, it must be divide by the owner or the maker, into another tasks
# - price: Price proposal by the owner
# - time: Time to done proposal by the owner
# - proposals: proposals of makers to do it
# - tests: its test
# - tags: tags to classify
class Task(models.Model):

    states={'Proposal','Asigned','Working','Testing','Done'}
    title=models.CharField(max_length==50)
    description=models.CharField(max_length=500)
    state=models.IntegerField(choices=states)
    price=models.IntegerField()
    time=models.IntegerField()
    owner=models.ForeignKey(User)
    maker=models.ForeignKey(User)
    proposals=models.ForeignKey(Proposal)
    test=models.ForeignKey(Test)
    tags=models.ForeignKey(Tag)


class User(models.Model):
    name=models.CharField(max_length=50)

class Proposal(models.Model):
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    time=models.IntegerField()

class Test(models.Model):

    states={'ToCheck','Failed','OK'}

    title=models.CharField(max_length==50)
    description=models.CharField(max_length=500)
    state=models.IntegerField(choices=states)

class Tag(models.Model):
    title=models.CharField(max_length==50)
    description=models.CharField(max_length=500)
    color=models.IntegerField()






