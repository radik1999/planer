from django.conf import settings
from django.db import models


class Priority(models.IntegerChoices):
    LOW = 0, 'Low'
    NORMAL = 1, 'Normal'
    HIGH = 2, 'High'


class Goal(models.Model):
    title = models.CharField(max_length=128)
    priority = models.IntegerField(default=Priority.LOW, choices=Priority.choices)
    sub_goal = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


class DailyTask(models.Model):
    title = models.CharField(max_length=128)
    priority = models.IntegerField(default=Priority.LOW, choices=Priority.choices)
    status = models.BooleanField(default=False)
    day = models.DateField(blank=True, null=True)
    sub_task = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.title}: {self.status}'
