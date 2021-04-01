from django.forms import ModelForm

from tasks.models import DailyTask


class DailyTaskForm(ModelForm):
    class Meta:
        model = DailyTask
        fields = ['title', 'priority', 'sub_task', 'goal']
