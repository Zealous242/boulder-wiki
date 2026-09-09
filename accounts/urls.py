from django.urls import path

from .views import custom_login, custom_logout, signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]
