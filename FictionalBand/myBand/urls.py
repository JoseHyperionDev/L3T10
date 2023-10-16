from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('albums/', views.album_list, name='album_list'),
    path('register/', views.user_registration, name='registration'),
    
]