from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

from django.urls import reverse

from dailyplan.scryps import time_convert


def positive_valid(value):
    if value <= 0:
        raise ValidationError('Time has to be greater then 0')


def time_valid(value):
    try:
        time_convert(value)
    except Exception as e:
        raise ValidationError('Some trouble has happened. Please, input another value')


class MyDay(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    day_date = models.DateField()

    def __str__(self):
        return self.day_date.__str__()


class Task(models.Model):
    title = models.CharField(max_length=128)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    day = models.ForeignKey(MyDay, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('plan:day', kwargs={'pk': self.day.id})

    def __str__(self):
        return f'{self.title}: {self.status}'
