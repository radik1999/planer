# Generated by Django 3.1.3 on 2020-11-27 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dailyplan', '0002_auto_20201126_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='days',
        ),
        migrations.RemoveField(
            model_name='myday',
            name='tasks',
        ),
        migrations.AddField(
            model_name='myday',
            name='tasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dailyplan.task'),
        ),
        migrations.DeleteModel(
            name='DaysTask',
        ),
    ]
