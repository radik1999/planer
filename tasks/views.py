from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from datetime import date

from tasks.models import DailyTask


class Today(LoginRequiredMixin, View):
    week_days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    today = date.today()
    week_day_today = week_days[date.weekday(today)]

    def get(self, request):

        today_tasks = DailyTask.objects.filter(date=str(self.today), owner=request.user)

        ctx = {'day': self.today, 'week_day': self.week_day_today, 'tasks': today_tasks}

        return render(request, 'tasks/today.html', context=ctx)






