from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('set_profile', views.set_profile, name='set_profile'),
    path('edit_profile/<int:num>', views.edit_profile, name='edit_profile'),
    path('register_book', views.register_book, name='register_book'),
    path('register_study/<int:num>/<int:is_public>', views.register_study, name='register_study'),
    path('my_page', views.my_page, name='my_page'),
]