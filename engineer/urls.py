from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('set_profile', views.set_profile, name='set_profile'),
]