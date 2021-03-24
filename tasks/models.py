from django.conf import settings
from django.db import models

from dailyplan.models import Task as TaskField


class Task(models.Model):
    title = models.CharField(max_length=128)
    day = models.DateField()
    priority = models.IntegerChoices() # todo
    time_spent = models.IntegerField() # todo
    status = models.BooleanField(default=False)
    sub_task = models.ForeignKey(TaskField, on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.title}: {self.status}'
