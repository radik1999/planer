from django.urls import path

from dailyplan.views import *

app_name = 'plan'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task'),
    path('task/create', TaskCreateView.as_view(), name='create'),
    path('task/update/<int:pk>', TaskUpdateView.as_view(), name='update'),
    path('task/delete/<int:pk>', TaskDeleteView.as_view(), name='delete'),
    path('week', WeekPlanView.as_view(), name='week'),
    path('day/<int:pk>', MyDayDetailView.as_view(), name='day'),
]
