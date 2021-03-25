from django.contrib import admin

from tasks.models import Goal, DailyTask

admin.site.register(Goal)
admin.site.register(DailyTask)
# Register your models here.
