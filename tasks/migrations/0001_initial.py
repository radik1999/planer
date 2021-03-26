# Generated by Django 3.1.7 on 2021-03-25 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('priority', models.IntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')], default=0)),
                ('sub_goal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.goal')),
            ],
        ),
        migrations.CreateModel(
            name='DailyTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('priority', models.IntegerField(choices=[(0, 'Low'), (1, 'Normal'), (2, 'High')], default=0)),
                ('status', models.BooleanField(default=False)),
                ('day', models.DateField(blank=True, null=True)),
                ('goal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.goal')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sub_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.dailytask')),
            ],
        ),
    ]