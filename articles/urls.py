from django.urls import path

from .views import categories, home, search

urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('search/', search, name='search'),
]
