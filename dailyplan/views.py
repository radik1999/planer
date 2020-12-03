from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View, generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from datetime import date, timedelta

from .forms import TaskForm
from .models import *
# Create your views here.


class OwnerClass:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dailyplan/home.html')


class TaskListView(OwnerClass, LoginRequiredMixin, generic.ListView):
    model = Task


class TaskDetailView(OwnerClass, LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Task
    fields = ['title']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return redirect(reverse_lazy('plan:tasks'))


class TaskUpdateView(OwnerClass, LoginRequiredMixin, generic.edit.UpdateView):
    model = Task
    fields = ['title', 'status']


class TaskDeleteView(OwnerClass, LoginRequiredMixin, generic.edit.DeleteView):
    model = Task

    def get_success_url(self):
        return self.request.session['theday']


class WeekPlanView(LoginRequiredMixin, View):
    @staticmethod
    def get_or_create_week(request):
        today = date.today()
        first_day_of_week = today - timedelta(days=today.weekday())
        whole_week = [first_day_of_week + timedelta(days=d) for d in range(7)]
        days = []
        tasks = []

        for day in whole_week:
            if not MyDay.objects.filter(day_date=str(day), owner=request.user):
                MyDay(day_date=str(day), owner=request.user).save()

            days.append(MyDay.objects.get(day_date=str(day), owner=request.user))

        # create dict with days and relative plans
        for day in days:
            day_tasks = Task.objects.filter(owner=request.user, day=day.id)
            tasks.append(day_tasks)

        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return zip(days, tasks, weekday_names)

    def get(self, request):
        ctx = {'week': self.get_or_create_week(request)}
        return render(request, 'dailyplan/week.html', context=ctx)


class MyDayDetailView(OwnerClass, LoginRequiredMixin, View):
    template_name = 'dailyplan/day_detail.html'

    @staticmethod
    def get_ctx_obj(pk, user):
        try:
            obj = MyDay.objects.get(pk=pk, owner=user)
        except Exception as e:
            obj = None
        return obj

    def get(self, request, pk):
        task_titles = [task.title for task in Task.objects.filter(owner=request.user)]
        task_titles = set(task_titles)

        request.session['theday'] = request.path

        obj = self.get_ctx_obj(pk, request.user)

        this_day_tasks = Task.objects.filter(owner=request.user, day=obj.id)

        ctx = {'day': obj, 'task_titles': task_titles, 'next': request.path, 'tasks': this_day_tasks}

        return render(request, self.template_name, context=ctx)

    def post(self, request, pk):
        new_task_title = request.POST['task']

        request.session['theday'] = request.path

        if new_task_title:
            this_day = self.get_ctx_obj(pk, request.user)
            new_task, status = Task.objects.get_or_create(title=new_task_title, owner=request.user, day=this_day)

        return self.get(request, pk)

