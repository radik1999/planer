from django.urls import path


from tasks.views import Today


app_name = 'tasks'

urlpatterns = [
    path('today', Today.as_view(), name='today')
]
