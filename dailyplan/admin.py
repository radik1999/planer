from django.contrib import admin


from dailyplan.models import MyDay, Task

# Register your models here.
admin.site.register(Task)
admin.site.register(MyDay)
