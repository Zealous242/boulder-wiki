from django.contrib import admin
from django.urls import include, path

from accounts.views import custom_login, custom_logout, signup

urlpatterns = [
    path('', include('articles.urls')),
    path('articles/', include('articles.urls')),
    path('categories/', include('articles.urls')),
    path('search/', include('articles.urls')),
    path('register/', signup, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('admin/', admin.site.urls),
]
