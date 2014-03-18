from django.contrib import admin

# Register your models here.
from Task.models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','owner', 'maker','state', 'left_time', )
    list_filter = ['owner','maker','state', ]
    search_fields = ['title','owner__name','maker__name',]
    fieldsets = [
        ('Definition', {'fields': ['title', 'description','initialCost','initialDuration','tags', ]}),
        ('In charge', {'fields': ['owner', 'maker', ]}),
        ('Proposals', {'fields': ['proposals',], 'classes': ['collapse']}),
        ('Eval', {'fields': [ 'tests' ], 'classes': ['collapse']}),
        ('Subtasks', {'fields': ['subtasks'], 'classes': ['collapse']}),
    ]

admin.site.register(Task,TaskAdmin)
admin.site.register(User)
admin.site.register(Proposal)
admin.site.register(Test)
admin.site.register(Tag)