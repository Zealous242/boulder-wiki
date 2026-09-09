from django.urls import path

from .views import suggestion_list

urlpatterns = [
    path('', suggestion_list, name='suggestions'),
]
