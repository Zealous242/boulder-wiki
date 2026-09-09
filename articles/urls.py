from django.urls import path

from .views import article_list, categories, home, search

urlpatterns = [
    path('', home, name='home'),
    path('articles/', article_list, name='article_list'),
    path('categories/', categories, name='categories'),
    path('search/', search, name='search'),
]
