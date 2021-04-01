from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from datetime import date

from tasks.models import DailyTask, Goal
from tasks.forms import DailyTaskForm


class Today(LoginRequiredMixin, View):
    week_days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    today = date.today()
    week_day_today = week_days[date.weekday(today)]

    def get(self, request):
        today_tasks = DailyTask.objects.filter(date=str(self.today), owner=request.user)
        goals = Goal.objects.filter(owner=request.user)

        ctx = {'day': self.today,
               'week_day': self.week_day_today,
               'tasks': today_tasks,
               'goals': goals
               }

        return render(request, 'tasks/today.html', context=ctx)

    def post(self, request):
        title = request.POST['title']
        priority = request.POST['priority']

        goal_str = None if request.POST['goal'] else request.POST['goal']
        goal = Goal.objects.get(title=goal_str) if goal_str else None

        task = DailyTask(title=title, date=self.today, priority=priority, goal=goal, owner=request.user)
        task.save()

        return redirect('tasks:today')



