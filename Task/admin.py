from django.contrib import admin

# Register your models here.
from Task.models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','owner', 'maker','state', 'left_time', 'priority' )
    list_filter = ['state','primary','priority', ]
    search_fields = ['title','owner__name', 'maker__name',]
    fieldsets = [
        ('Definition', {'fields': ['title', 'description', 'initialCost', 'initialDuration', 'primary', 'priority', 'tags', ]}),
        ('In charge', {'fields': ['owner', 'maker', ]}),
        ('Proposals', {'fields': ['proposals','selectedProposal'], 'classes': ['collapse']}),
        ('Eval', {'fields': ['tests'], 'classes': ['collapse']}),
        ('Subtasks', {'fields': ['subtasks'], 'classes': ['collapse']}),
        ('Steps', {'fields': ['steps'], 'classes': ['collapse']}),
    ]

admin.site.register(Task,TaskAdmin)
admin.site.register(User)
admin.site.register(Proposal)
admin.site.register(Test)
admin.site.register(Tag)
admin.site.register(Priority)
admin.site.register(Step)