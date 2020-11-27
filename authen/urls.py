from django.urls import path


from authen.views import *


app_name = 'authen'
urlpatterns = [
    path('signout', logout_view, name='signout'),
    path('signup', signup, name='signup'),
]
