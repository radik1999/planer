from django.contrib.auth.models import User
from django.test import TestCase
from dailyplan.models import *
from datetime import date


class TaskTestCase(TestCase):
    def setUp(self) -> None:
        usr = User.objects.create_user('test', 'mail@mail.com', '123')
        Task(title='test', owner=usr).save()

    def test_task_creation(self):
        task = Task.objects.get(title='test')
        self.assertEqual(task.title, 'test')


class DayTestCase(TestCase):
    def setUp(self) -> None:
        self.usr = User.objects.create_user('test', 'mail@mail.com', '123')
        MyDay(day_date=str(date.today()), owner=self.usr).save()

    def test_day_creation(self):
        day = MyDay.objects.get(owner=self.usr)
        self.assertEqual(day.day_date, date.today())


