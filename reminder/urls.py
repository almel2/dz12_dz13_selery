from django.urls import path

from reminder.views import index, plus

urlpatterns = [
    path('', index, name='home'),
    path('pl', plus, name="plus")
    ]